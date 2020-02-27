#TODO: Accept args for page limit and offset. 

import scrapy
import re
import os
from scrapy.spiders import CrawlSpider, Rule 
from scrapy.linkextractors import LinkExtractor
from scrapy.link import Link

class PitchforkSpider(CrawlSpider):  
    name = 'pitchfork_news'
    start_urls = ['https://www.pitchfork.com/news/?page=1']
    
    rules = (
            Rule(LinkExtractor(restrict_xpaths=('//div[contains(@class, "news-module")]','//link[@rel="next"]'), tags=['a', 'link']), callback="parse_items", follow=False),
    )

    def __init__(self, follow=None, *args, **kwargs): 
        super(PitchforkSpider, self).__init__(*args, **kwargs)
        self.follow = follow

    
    def parse_items(self, response):
        print('Parsing webpage...')
        print(response)
        media = response.xpath('//img/@src | //iframe/@src')
        data = response.xpath('//div[@class="article-content"]')
        ws = ' '
        print('html content is')
        if(re.match(r'\?page=\d$',response.url) == None):
            for item in data:
                print('------------- Parsing article -------------')
                print(item.getall())
                yield {
                    "title": item.xpath('.//header/h1/text()').get(),
                    "subtitle": item.xpath('.//header/p/text()').get(),
                    # "content": item.xpath('.//div[@class="contents"]/p/text()').getall(),
                    "text_content": ws.join(item.xpath('.//div[@class="contents"]//text()').getall()),
                    "media": media.getall(),
                }
            print('------------- Done parsing -------------')
