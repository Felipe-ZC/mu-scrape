import scrapy

class NewsSpider(scrapy.Spider):
    name = "news"
    start_urls = ['https://capturedtracks.com/news/']
    
    # Keep note of the strategies used for each website,
    # they'll change as we go along!
    
    def parse(self, response):
        print('Parsing webpage...')
        data = response.xpath('//article')
        print('Found ' + str(len(data)) + ' articles')
        # print(data[0].getall())
        counter = 1
        for item in data:
            print('------------- Parsing article #{} -------------'.format(counter))
            print(item.getall())
            counter = counter + 1
            # print(item.xpath('.//header').getall())
            yield {
                "title" : item.xpath('.//header/a/h1/text()').get(),
                "date" : item.xpath('.//header/a/time/text()').get(),
                "preview" : item.xpath('.//div[@class="news-item--preview"]/p/text()').get().rstrip(),
            }

