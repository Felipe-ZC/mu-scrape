from setuptools import setup

setup(name='mu-scrape',
      version='0.1',
      description='Scrapy spider that crawls music related websites.',
      url='https://github.com/Felipe-ZC/mu-scrape',
      author='Felipe-ZC',
      license='MIT',
      install_reqs=[
        'Scrapy',
        'scrapy-splash'
      ],
      packages=['mu_scrape'])
