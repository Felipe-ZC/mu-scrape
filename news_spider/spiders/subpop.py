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

                # TODO: Change this xpath to select any tag with a path ending in text()
                # except for <div> and <header>.
                # "preview" : item.xpath('./p/text() | ./ul/li/p/text()').getall()
                # descendant refers to all children, grandchildren etc. of the current node,
                # in this case the current node is article. The xpath below selects all text
                # node desecendants of an article tag. 
                "preview" : item.xpath('./descendant::text()').getall(),
            }
        print('------------- Done parsing -------------')
        # next_page = response.xpath('//div[@class="wrapper"]/a/@href').get()
        # if next_page:
            # yield response.follow(next_page, callback=self.parse)

