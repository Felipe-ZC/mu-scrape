import re
import scrapy
from scrapy.spiders import CrawlSpider, Rule 
from scrapy.linkextractors import LinkExtractor
from scrapy import Request

# TODO: Accept args for page limit and offset. 
# TODO: Make one base class spider and have each site specific spider 
# implement its own parse method

class KexpSpider(scrapy.Spider):
    name = 'kexp_news'
    start_urls = ['https://www.kexp.org/read/?page=1']

 
    def __init__(self, follow=None, *args, **kwargs): 
        super(KexpSpider, self).__init__(*args, **kwargs)
        self.follow = follow

    def start_requests(self):
        return [Request("https://www.kexp.org/read/?page=1")]

    def parse(self, response):
        print('Parsing webpage...')
        print(response.request.headers['User-Agent'])
        media = response.xpath('//img/@data-src | //iframe/@src')
        data = response.xpath('//article')
        ws = ' ' # TODO: Is there a better way of joining content?
        # Only parse full articles...
        if(re.match('https://capturedtracks.com/news/page/[0-9]/', response.url) == None):
            for item in data:
                print('------------- Parsing element -------------')
                print(item.getall())
                yield {
                    "title": item.xpath('.//h1[@class="article--title"]/text()').get(),
                    "date": item.xpath('.//time[@class="article--date"]/text()').get(),
                    # TODO: Verify this xpath
                    "content": ws.join(item.xpath('.//div[@class="article--content"]/p/text()').getall()),
                    "media": media.getall(),
                }
            print('------------- Done parsing -------------')
        else:
            print('Moving to the next page...')

# class KexpSpider(CrawlSpider):
    # name = 'kexp_news'
    # start_urls = ['https://www.kexp.org/read/?page=1']

    # rules = (
        # # Rule(LinkExtractor(allow=(), restrict_xpaths=('//a[text() = "Read More..."]')), callback="parse_items", follow= True),
        # # Load all articles...
        # Rule(LinkExtractor(allow=(), restrict_xpaths=('//a[text() = normalize-space("Read More")]','//a[text() = normalize-space("View More News")]')), callback="parse_items",  follow=True, process_request="check_headers"),
    # )
 
    # def __init__(self, follow=None, *args, **kwargs): 
        # super(KexpSpider, self).__init__(*args, **kwargs)
        # self.follow = follow
 
    # def check_headers(self, response, request):
        # print(request.headers)
        # return request 

    # def parse_items(self, response):
        # print('Parsing webpage...')
        # print(response.request.headers['User-Agent'])
        # media = response.xpath('//img/@data-src | //iframe/@src')
        # data = response.xpath('//article')
        # ws = ' ' # TODO: Is there a better way of joining content?
        # # Only parse full articles...
        # if(re.match('https://capturedtracks.com/news/page/[0-9]/', response.url) == None):
            # for item in data:
                # print('------------- Parsing element -------------')
                # print(item.getall())
                # yield {
                    # "title": item.xpath('.//h1[@class="article--title"]/text()').get(),
                    # "date": item.xpath('.//time[@class="article--date"]/text()').get(),
                    # # TODO: Verify this xpath
                    # "content": ws.join(item.xpath('.//div[@class="article--content"]/p/text()').getall()),
                    # "media": media.getall(),
                # }
            # print('------------- Done parsing -------------')
        # else:
            # print('Moving to the next page...')

