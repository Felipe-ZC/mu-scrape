#TODO: Accept args for page limit and offset. 

import scrapy
import re
import os
from scrapy.spiders import CrawlSpider, Rule 
from scrapy.linkextractors import LinkExtractor

class PitchforkSpider(CrawlSpider):  
    name = 'pitchfork_news' 
    start_urls = ['https://www.pitchfork.com/news/?page=1']
    
    rules = (
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//div[contains(@class, "news-module")]')), callback="parse_items"),
        # Load all articles...
        # Rule(LinkExtractor(allow=(), restrict_xpaths=('//a[text() = "Read More..."]','//a[text() = "Load More"]')), callback="parse_items", follow= True),
    )

    def __init__(self, follow=None, *args, **kwargs): 
        super(PitchforkSpider, self).__init__(*args, **kwargs)
        self.follow = follow
    
    def parse_items(self, response):
        print('Parsing webpage...')
        print(response)
        data = response.xpath('//div[@class="article-content"]')
        ws = ' '
        for item in data:
            print('------------- Parsing article -------------')
            print(item.getall())
            #TODO: xpath: .// vs //
            yield {
                "title": item.xpath('.//header/h1/text()').get(),
                "subtitle": item.xpath('.//header/h2/p/text()').get(),
                "content": item.xpath('.//div[@class="contents"]').get(),
            }
        print('------------- Done parsing -------------')
        #TODO: Add arg to enable/disable link following
        if self.follow:
            next_page = response.xpath('//div[@class="pagination"]/span[@class="next"]/a/@href').get()
            if next_page:
                # yield response.follow(next_page, callback=self.parse, meta={'proxy' : os.environ['scrapy_http_proxy']})
                yield response.follow(next_page, callback=self.parse)

