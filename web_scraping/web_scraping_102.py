import requests
from bs4 import BeautifulSoup

wordpress_html = requests.get(
    "https://en-gb.wordpress.org/plugins/browse/popular/")
"""
Extract Information with BS4
Why not regular expressions ?
- They are brittle
- Very hard to read
- Very hard to support
- You end up recreating a parser
"""

PAGE = "http://localhost:8080/auto_mpg.html"

# it will send get request to given address
page_result = requests.get(PAGE)

# it will keep result
page_source = page_result.text

parse_webpage = BeautifulSoup(page_source, "html.parser")

print(parse_webpage.title.getText())

# get first 1000
print(parse_webpage.body.get_text()[:1000])

# find_all
div = parse_webpage.find_all("div", class_="car_block")[0]
print(div.prettify())

# copy element selector from Chrome Developer Tools and practice
div_selector = parse_webpage.select("#car-1 > span.mpg")
print(div_selector)
"""
ADVICE AND STRATEGY FOR SCRAPING
1. Selecting your content
2. Bs4 elements
3. Find functions
4. CSS selectors
"""
