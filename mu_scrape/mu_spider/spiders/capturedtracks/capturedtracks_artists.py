import scrapy
import re

class CapturedTracksSpider(scrapy.Spider):
    name = "capturedtracks_artists"
    start_urls = ["https://capturedtracks.com/artists/roster/"]

    def __init__(self, follow=None, *args, **kwargs):
        super(CapturedTracksSpider, self).__init__(*args, **kwargs)
        self.follow = follow

    def parse(self, response):
        data = response.xpath('//div[@class="artists-grid"]')
        print("data is")
        print(data)
        for item in data:
            print("------------- Parsing element -------------")
            yield {"artists": item.xpath("./article/a/h1/text()").getall()}
        print("------------- Done parsing -------------")
