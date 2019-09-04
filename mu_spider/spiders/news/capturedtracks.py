import scrapy

# TODO: Accept args for page limit and offset. 
# TODO: Make one base class spider and have each site specific spider 
# implement its own parse method

class CTSpider(scrapy.Spider):
    name = 'capturedtracks'
    start_urls = ['https://capturedtracks.com/news/']
    
    def __init__(self, follow=None, *args, **kwargs): 
        super(CTSpider, self).__init__(*args, **kwargs)
        self.follow = follow
    
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
                # NOTE: Some articles do not feature the date in the header tag...
                "date" : item.xpath('.//header/a/time/text()').get(),
                "preview" : item.xpath('.//div[@class="news-item--preview"]/p/text()').get(),
            }
        print('------------- Done parsing -------------')
        if self.follow:
            next_page = response.xpath('//div[@class="wrapper"]/a/@href').get()
            if next_page:
                yield response.follow(next_page, callback=self.parse)

