import scrapy

#TODO: Accept args for page limit and offset. 
#TODO: Start thinking about pitchfork, subpop scraping strategy.

#NOTE: Subpop and capturedtracks use the same scraping strategy. (/news/pageNum)

class NewsSpider(scrapy.Spider):
    name = "capturedTracks"
    start_urls = ['https://www.subpop.com/news']
    
    # Keep note of the strategies used for each website,
    # they'll change as we go along!
    
    def parse(self, response):
        print('Parsing webpage...')
        data = response.xpath('//article[@class="entry"]')
        print('Found ' + str(len(data)) + ' articles')
        for item in data:
            print('------------- Parsing article -------------'.format(counter))
            print(item.getall())
            #TODO: xpath: .// vs //
            yield {
                "title" :item.xpath('.//header/h2/a/text()').get(),
                "date" : item.xpath('.//header/p/a/text()').get(),
                "preview" : item.xpath('./p').getall(),
            }
        print('------------- Done parsing -------------')
        # next_page = response.xpath('//div[@class="wrapper"]/a/@href').get()
        # if next_page:
            # yield response.follow(next_page, callback=self.parse)

