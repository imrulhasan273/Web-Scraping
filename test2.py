from scrapy import Selector
import requests

def scrap():
    
    url = 'https://en.wikipedia.org/wiki/Web_scraping'
    
    html = requests.get(url).content

    sel = Selector(text = html)
    
    selectorList=sel.css("div > div > h2 > span:nth-of-type(1)").extract()

    print(selectorList)


if __name__ == "__main__":
    scrap()
    
''' _______________________
    Web Scraping Tool::Software
    _____________________________
    Developed By    :   Md. Imrul Hasan (imrulhasan273@gmail.com)
'''

