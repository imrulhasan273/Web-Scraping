
## XPath Notation

---

- Convention: Use single quote to define a `XPath` String. Double quote inside it.

```py
xpath = '/html/body/div[2]'
xpath = '//table'
xpath = 'html/body/div[2]//table'
xpath = '//span[@class="span-class"]'
xpath = '//div[@id="uid"]
```

## Attributes

```py
@class
@id
@href
```

```py
xpath = '//p[@class="class-1"]' #all p tag with class name of 'class-1'
xpath = '//*[@id="id-1"]' #all tag with id name of 'id-1'
```

## Contains notation

```py
contains(@attri-name, "string-expr")
```

```py
xpath = '//*[contains( @class "class-1" )]' # drawback: If the class name is 'class-12' it will be counted as 'class-1' is a sub string of 'class-12'. Used when partially match
xpath = '//*[@class="class-1"]'             # 'class-1' will be counted only. Used when Exact match
```

```py
xpath = '/html/body/div/p[2]'
xpath = '/html/body/div/p[2]/@class'
xpath = '//p[@id="p2"]/a/@href'
```

## Scrapy Selector

```py
from scrapy import Selector

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

sel.xpath("//p")

```

## XPath Chaining

```py
sel.xpath( '//div' ).xpath( './span/p[3]' )

course_as = sel.css( 'div.course-block > a' )
course_as.xpath( './@href' )
```




## CSS Locators

- `/` replaced by `>` (except first char)

```py
xpath = '/html/body/div'
cssloc = 'html > body > div'
```

- Note: First char is `/`. We ignoed it.

- Note: Double `//` in XPath is replaced by a blank space; So a blank space looks `/` all generation.

```py
xpath = '//div/span//p'
cssloc = 'div > span p'
```

```py
xpath = '//div/p[2]'
cssloc = 'div > p:nth-of-type(2)'
```

```py
xpath = '/html/body//div/p[2]'
cssloc = 'html > body div > p:nth-of-type(2)'
```

```py
cssloc = 'div#uid > p.class1'
cssloc = '.class1'              # works for : class='class1 class2 class3' ; if match one of classes. xpath have drawback in this case.
cssloc = '#id'
css_locator = '#uid > *'
```

```py
sel.css("div > p")
sel.css("div > p").extract()
```

## CSS Locator

```py
xpath = '<x-path-to-element>/@attr-name'
xpath = '//div[@id="uid"]/a/@href'
```

```py
cssloc = '<css-to-element>::attr(attr-name)'
cssloc = 'div#uid > a:attr(href)'
```


## Text Extraction

```py
sel.xpath('//p[@id="p-example"]/text()').extract()      # All the text elements 
sel.xpath('//p[@id="p-example"]//text()').extract()     # All text text elements with its descendant 
```

```py
sel.xpath('p#p-example::text').extract()                # All the elements 
sel.xpath('p#p-example ::text').extract()               # All the elements with its future generation [Add a space before ::]
```

## `Response` Obj [Like `Selector` but it has `Scrawling` capability]

```py
# xpath
response.xpath('//div/span[@class="bio"]')              # span element whose class name is "bio" 
# css
response.css('div > span.bio')  
# chain
response.xpath('//div').css('span.bio')  
# extract
response.xpath('//div').css('span.bio').extract()
response.xpath('//div').css('span.bio').extract_first()
```

```py
response_url = 'http://www.datacamp.com/courses/all'
```

- the response let us 'follow' a new link with the `follow()` method

```py
# next_url is the string path of the next url we want to scrape
response.follow( next_url )
```

```py
this_url = response.url
```


```py
divs = response.css( 'div.course-block' )
first_div = divs[0]
h4_text = first_div.css('h4::text').extract_first()
```

```py
links = response.css('div.course-block > a::attr(href)').extract()
```

```py
# Step 1: course block
course_divs = response.css('div.course-block')
# Step 2: hyperlink elements
hrefs = course_divs.xpath('./a/@href')
# Step 3: Extract the links
links = hrefs.extract()

for link in links:
    print(link)
```

## Spider









