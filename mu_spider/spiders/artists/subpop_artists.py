#TODO: Accept args for page limit and offset. 
import scrapy
import re

class SubpopSpider(scrapy.Spider):  
    name = 'subpop_artists' 
    start_urls = ['https://www.subpop.com/artists/list']
    
    def __init__(self, follow=None, *args, **kwargs): 
        super(SubpopSpider, self).__init__(*args, **kwargs)
        self.follow = follow
    
    def parse(self, response):
        data = response.xpath('//section[@class="alpha-list"]')
        for item in data:
            print('------------- Parsing element -------------')
            yield { "artists": item.xpath('./ul/li/a/text()').getall() }
        print('------------- Done parsing -------------')

