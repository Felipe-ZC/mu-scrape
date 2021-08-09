# TODO: Accept args for page limit and offset.
import scrapy
import re

class SubpopSpider(scrapy.Spider):
    name = "subpop_artists"
    start_urls = ["https://www.subpop.com/artists"]

    def __init__(self, follow=None, *args, **kwargs):
        super(SubpopSpider, self).__init__(*args, **kwargs)
        self.follow = follow

    def parse(self, response):
        data = response.xpath('//ul[@id="current-artists"]')
        for item in data:
            print("------------- Parsing element -------------")
            yield {
                "artists": item.xpath(
                    './li/article/div/h3[@class="artist-name"]/a/text()'
                ).getall()
            }
        print("------------- Done parsing -------------")
