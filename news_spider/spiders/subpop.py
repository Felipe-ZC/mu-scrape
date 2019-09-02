import scrapy

#TODO: Accept args for page limit and offset. 
#TODO: Start thinking about pitchfork, subpop scraping strategy.

#NOTE: Subpop and capturedtracks use the same scraping strategy. (/news/pageNum)

class NewsSpider(scrapy.Spider):
    name = 'subpop'
    start_urls = ['https://www.subpop.com/news']
    
    # Keep note of the strategies used for each website,
    # they'll change as we go along!
    
    def parse(self, response):
        print('Parsing webpage...')
        data = response.xpath('//article[@class="entry"]')
        print('Found ' + str(len(data)) + ' articles')
        for item in data:
            print('------------- Parsing article -------------')
            print(item.getall())
            #TODO: xpath: .// vs //
            yield {
                "title" :item.xpath('.//header/h2/a/text()').get(),
                "date" : item.xpath('.//header/p/text()').getall(), 
                # NOTE: There are <span> tags after some of the <p> elements for preview
                # elements which our path is not accounting for. 
                "preview" : item.xpath('./p/text() | ./ul/li/p/text()').getall(),
            }
        print('------------- Done parsing -------------')
        # next_page = response.xpath('//div[@class="wrapper"]/a/@href').get()
        # if next_page:
            # yield response.follow(next_page, callback=self.parse)

