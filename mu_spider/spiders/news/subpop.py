import scrapy
import re

#TODO: Accept args for page limit and offset. 
#TODO: Start thinking about pitchfork, subpop scraping strategy.

#NOTE: Subpop and capturedtracks use the same scraping strategy. (/news/pageNum)

class SubpopSpider(scrapy.Spider):
    name = 'subpop'
    start_urls = ['https://www.subpop.com/news']
    
    # Keep note of the strategies used for each website,
    # they'll change as we go along!
    
    def parse(self, response):
        print('Parsing webpage...')
        data = response.xpath('//article[@class="entry"]')
        print('Found ' + str(len(data)) + ' articles')
        ws = ' '
        for item in data:
            print('------------- Parsing article -------------')
            print(item.getall())
            #TODO: xpath: .// vs //
            yield {
                "title" :item.xpath('.//header/h2/a/text()').get(),
                # TODO: Filter words that are not alpha numeric (escape sequences)
                # TODO: Date is prefixed with a ':', lets get rid of it
                "date" : ws.join(item.xpath('.//header/p/text()').getall()).replace(':', '').strip(), 
                # NOTE: There are <span> tags after some of the <p> elements for preview
                # elements which our path is not accounting for.
                # TODO: Change this xpath to select any tag with a path ending in text()
                # except for <div> and <header>.
                # descendant refers to all children, grandchildren etc. of the current node,
                # in this case the current node is article. The xpath below selects all text
                # node desecendants of an article tag.
                # NOTE: This computation does not preserve the original structure of the text...
                # "preview" : ws.join(item.xpath('./*[not(self::header)]/descendant::text()').getall()).strip(),
                # NOTE: When using the pattern \\[rnt], python did not match the write strings (newline, carriage return, tab),
                # using [\r\n\t] so as to search for an ASCII value. 
                "preview" : ws.join([re.sub("[\r\n\t]", "", st) for st in item.xpath('./*[not(self::header)]/descendant::text()').getall()]),
            }
        print('------------- Done parsing -------------')
        next_page = response.xpath('//div[@class="pagination"]/span[@class="next"]/a/@href').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

