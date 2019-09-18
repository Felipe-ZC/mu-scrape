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
        print('Parsing webpage...')
        # print(response)
        data = response.xpath('//section[@class="alpha-list"]')
        # print(data)
        for item in data:
            print('------------- Parsing article -------------')
            # Parse all artists in each alpha list
            alpha_artists = item.xpath(".//ul/li/a/text()").getall();
            print(alpha_artists)
            #TODO: Think of more info to pull for artists... 
            yield {
                "artists": item.xpath(".//ul/li/a/text()").getall(),
            }
        print('------------- Done parsing -------------')
        #TODO: Find a way to use case for link following on artists page or remove this... 
        # if self.follow:
            # next_page = response.xpath('//div[@class="pagination"]/span[@class="next"]/a/@href').get()
            # if next_page:
                # yield response.follow(next_page, callback=self.parse)

