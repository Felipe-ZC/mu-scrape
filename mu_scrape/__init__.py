from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from shutil import rmtree
import argparse

# TODO: Argument for deleting all files in output folder before scraping...

parser = argparse.ArgumentParser(
    description="A utility to run the spiders in this project."
)
parser.add_argument("--f", dest="follow", action="store_true")
args = parser.parse_args()

settings = get_project_settings()
process = CrawlerProcess(settings)

print("Running all spiders...")
process.crawl("subpop_news", args.follow)
process.crawl("capturedtracks_news", args.follow)
process.crawl("subpop_artists")
process.crawl("capturedtracks_artists")

process.start()  # the script will block here until the crawling is finished
