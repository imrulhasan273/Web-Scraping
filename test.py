from datetime import datetime, timedelta
import schedule
import time
from scrapy import Selector

def scrap():

    html = '''
        <html>
        <body>
            <div id="div1" class="class-1">
            <p class="class-1 class-2">Hello World!</p>
            <div id="div2">
                <p id="p2" class="class-2">Choose 
                    <a href="http://datacamp.com">DataCamp!</a>!
                </p>
            </div>
            </div>
            <div id="div3" class="class-2">
            <p class="class-2">Thanks for Watching!</p>
            </div>
        </body>
        </html>

        '''

    sel = Selector(text = html)

    selectorList=sel.xpath("//p")              # Selector List
    selectorListValue=sel.xpath("//p").extract()    # Extracted Data from Selector List
    selectorListValueFirst=sel.xpath("//p").extract_first()


    print("_____________________________selectorList_____________________________")
    print(selectorList)
    
    print("_____________________________selectorListValue_____________________________")
    print(selectorListValue)
    
    print("_____________________________selectorListValueFirst_____________________________")
    print(selectorListValueFirst)

    
    ps = sel.xpath("//p")
    sec_p = ps[1]
    selectorListValue2=sec_p.extract()
    
    print("_____________________________selectorListValue2_____________________________")
    print(selectorListValue2)



if __name__ == "__main__":
    scrap()
    
''' _______________________
    Web Scraping Tool::Software
    _____________________________
    Developed By    :   Md. Imrul Hasan (imrulhasan273@gmail.com)
'''

