from scrapy.crawler import crawlerprocess
from scrapy.utils.project import get_project_settings
from shutil import rmtree

settings = get_project_settings()
process = crawlerprocess(settings)

#note: delete old output dir before crawling...
print("removing current output dir at: " + settings.get('feed_custom_dir'))

rmtree(settings.get('feed_custom_dir'), ignore_errors=true)
#todo: get all spiders an run a loop here to crawl dynamically...
process.crawl('subpop')
process.crawl('capturedtracks')
process.start() # the script will block here until the crawling is finished
