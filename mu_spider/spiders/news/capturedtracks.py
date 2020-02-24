import re
import scrapy
from scrapy.spiders import CrawlSpider, Rule 
from scrapy.linkextractors import LinkExtractor

# TODO: Accept args for page limit and offset. 
# TODO: Make one base class spider and have each site specific spider 
# implement its own parse method

class CTSpider(CrawlSpider):
    name = 'capturedtracks_news'
    # allowed_domains = ['https://capturedtracks.com/']
    start_urls = ['https://capturedtracks.com/news/']

    rules = (
        # Rule(LinkExtractor(allow=(), restrict_xpaths=('//a[text() = "Read More..."]')), callback="parse_items", follow= True),
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//a[text() = "Read More..."]','//a[text() = "Load More"]')), callback="parse_items", follow= True),
    )
 
    def __init__(self, follow=None, *args, **kwargs): 
        super(CTSpider, self).__init__(*args, **kwargs)
        self.follow = follow
    
    def parse_items(self, response):
        print('Parsing webpage...')
        media = response.xpath('//img/@data-src | //iframe/@src')
        data = response.xpath('//article')
        ws = ' '
        # Only parse full articles...
        if(re.match('https://capturedtracks.com/news/page/[0-9]/', response.url) == None):
            for item in data:
                print('------------- Parsing element -------------')
                print(item.getall())
                #TODO: xpath: .// vs //
                yield {
                    "title": item.xpath('.//h1[@class="article--title"]/text()').get(),
                    "date": item.xpath('.//time[@class="article--date"]/text()').get(),
                    "content": ws.join(item.xpath('.//div[@class="article--content"]/p/text()').getall()),
                    "media": media.getall(),
                }
            print('------------- Done parsing -------------')
        else:
            print('Moving to the next page...')

