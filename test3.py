from scrapy import Selector
import requests
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import Spider

class DCspider(scrapy.Spider):
    name = "dc_spider"
    
    def start_requests(self):
        urls = ['http://www.datacamp.com/courses/all']
        
        for url in urls:
            yield scrapy.Request( url = url, callback=self.parse )  # Send Off
            
    def parse(self, response, **kwargs):
        # simple example : write out the html
        html_file = 'DC_course.html'
        with open( html_file, 'wb' ) as fout:
            fout.write( response.body )

class SpiderClassName(scrapy.Spider):
    name = "spider_name"
    # code for your spider
    

def main():
    # Initialize a CrawlerProcess
    process = CrawlerProcess()
    
    # Tell the process which spider to use
    process.crawl(SpiderClassName)
    
    # Start the crawling process
    process.start()
    
    

if __name__ == "__main__":
    main()
    
''' _______________________
    Web Scraping Tool::Software
    _____________________________
    Developed By    :   Md. Imrul Hasan (imrulhasan273@gmail.com)
'''

