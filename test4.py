from scrapy import Selector
import requests
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import Spider

class DC_Chapter_Spider(scrapy.Spider):
    name = "dc_chapter_spider"
    
    def start_requests(self):
        print('__________start_requests__________')
        urls = ['http://www.datacamp.com/courses/all']
        for url in urls:
            yield scrapy.Request( url = url, callback=self.parse_front ,dont_filter=True)  # Send Off
            #  meta={'dont_merge_cookies': True}
            
    def parse_front(self, response):
        print('__________parse_front__________')
        # Code to parse the front courses page
        # Narrow in on the course blocks
        course_block = response.css('div.course-block')
        # Direct to the course links
        course_links = course_block.xpath('./a/@href')
        # Extract the links (as a list of strings)
        links_to_follow = course_links.extract()
        # Follow the links to the next parser
        for url in links_to_follow:
            yield response.follow(url=url, callback = self.parse_pages)
            
            
    def parse_pages(self, response):
        print('__________parse_pages__________')
        # Code to parse course pages
        # Fill in dc_dict here
        crs_title = response.xpath('//h1[contains(@class,"title")]/text()')
        # Extract and clean the course title text
        crs_title_ext = crs_title.extract_first().strip()
        # Direct to the chapter titles text
        ch_titles = response.css( 'h4.chapter__title::text' )
        # Extract and clean the chapter titles text
        ch_titles_ext = [t.strip() for t in ch_titles.extract()]
        # Store this in our dictionary
        dc_dict[crs_title_ext] = ch_titles_ext
        
        print("_________________________________________________________________________________________________")
        print(dc_dict)
        print("_________________________________________________________________________________________________")        
            
    

if __name__ == "__main__":
    dc_dict = dict()
    
    # Initialize a CrawlerProcess
    process = CrawlerProcess()
    
    # Tell the process which spider to use
    process.crawl(DC_Chapter_Spider)
    
    # Start the crawling process
    process.start()
    
    
''' _______________________
    Web Scraping Tool::Software
    _____________________________
    Developed By    :   Md. Imrul Hasan (imrulhasan273@gmail.com)
'''

