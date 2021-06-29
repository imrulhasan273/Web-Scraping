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
            
    # CASE 1:
    def parse(self, response, **kwargs):
        # simple example : write out the html
        html_file = 'DC_course.html'
        with open( html_file, 'wb' ) as fout:
            fout.write( response.body )
            
            
    # CASE 2:
    def parse(self, response):
        # simple example : write out the html
        links = response.css('div.course-block > a::attr(href)').extract()
        filepath = 'DC_links.csv'
        with open( filepath, 'w' ) as f:
            f.writelines( [link + '/n' for link in links] )
            
            
    # CASE 3:
    def parse(self, response):
        # simple example : write out the html
        links = response.css('div.course-block > a::attr(href)').extract()
        for link in links:
            yield response.follow( url = link, callback = self.parse2 )
    
    def parse2(self, response):
        # parse the course site here...
        pass


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

