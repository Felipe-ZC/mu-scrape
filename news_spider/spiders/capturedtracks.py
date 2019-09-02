import scrapy

#TODO: Accept args for page limit and offset. 
#TODO: Start thinking about pitchfork, subpop scraping strategy.

#NOTE: Subpop and capturedtracks use the same scraping strategy. (/news/pageNum)

class NewsSpider(scrapy.Spider):
    name = 'capturedtracks'
    start_urls = ['https://capturedtracks.com/news/']
    
    # Keep note of the strategies used for each website,
    # they'll change as we go along!
    
    def parse(self, response):
        print('Parsing webpage...')
        data = response.xpath('//article')
        print('Found ' + str(len(data)) + ' articles')
        for item in data:
            print('------------- Parsing element {} -------------')
            print(item.getall())
            #TODO: xpath: .// vs //
            yield {
                "title" :item.xpath('.//header/a/h1/text()').get(),
                "date" : item.xpath('.//header/a/time/text()').get(),
                "preview" : item.xpath('.//div[@class="news-item--preview"]/p/text()').get(),
            }
        print('------------- Done parsing -------------')
        next_page = response.xpath('//div[@class="wrapper"]/a/@href').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

