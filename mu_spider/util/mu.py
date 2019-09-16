from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from shutil import rmtree
import argparse

parser = argparse.ArgumentsParser(description="A utility to run the spiders in this project.")

# parser.add_argument('--f', dest='follow')

settings = get_project_settings()
process = CrawlerProcess(settings)

#note: delete old output dir before crawling...
print("Runnings all spiders...")
#todo: get all spiders an run a loop here to crawl dynamically...
process.crawl('subpop_news', follow)
process.crawl('capturedtracks_news')
process.start() # the script will block here until the crawling is finished
