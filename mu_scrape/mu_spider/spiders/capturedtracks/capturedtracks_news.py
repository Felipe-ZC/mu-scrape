import re
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class CTSpider(CrawlSpider):
    name = "capturedtracks_news"
    # allowed_domains = ['https://capturedtracks.com/']
    start_urls = ["https://capturedtracks.com/news/"]

    def __init__(self, follow=None, *args, **kwargs):
        super(CTSpider, self).__init__(*args, **kwargs)
        rules = (
            # Rule(LinkExtractor(allow=(), restrict_xpaths=('//a[text() = "Read More..."]')), callback="parse_items", follow= True),
            # Load all articles...
            Rule(
                LinkExtractor(
                    allow=(),
                    restrict_xpaths=(
                        '//a[text() = "Read More..."]',
                        '//a[text() = "Load More"]',
                    ),
                ),
                callback="parse_items",
                follow=follow,
            ),
        )

    def parse_items(self, response):
        print("Parsing webpage...")
        media = response.xpath("//img/@data-src | //iframe/@src")
        data = response.xpath("//article")
        ws = " "  # TODO: Is there a better way of joining content?
        # Only parse full articles...
        if (
            re.match("https://capturedtracks.com/news/page/[0-9]/", response.url)
            == None
        ):
            for item in data:
                print("------------- Parsing element -------------")
                print(item.getall())
                yield {
                    "title": item.xpath('.//h1[@class="article--title"]/text()').get(),
                    "date": item.xpath('.//time[@class="article--date"]/text()').get(),
                    # TODO: Verify this xpath
                    "content": ws.join(
                        item.xpath(
                            './/div[@class="article--content"]/p/text()'
                        ).getall()
                    ),
                    "media": media.getall(),
                }
            print("------------- Done parsing -------------")
        else:
            print("Moving to the next page...")
