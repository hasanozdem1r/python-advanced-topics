# Content vs Styling
# -> HTML ; Page specific content, structure, text or voice, not written for scraping
# -> CSS ; Shared styling, selectors and declarations, divisions and spans, cascading rules
"""
WHY SCRAPE WEB PAGES
1. Storage and queries
2. Data augmentation
3. Analysis and Communication
"""
"""
DYNAMIC Websites
More difficult to scrape
Modern sites are often dynamic
Requires a tool like Selenium
STATIC Websites
Easy to scrape
Data dumps are often static
Requests and BeatifulSoup4
"""
"""
WEB Scraping Strategies
Processing Online ; Easy to develop, great for fewer pages, use for research
Processing Offline ; More complex, great for larger volumes, use for engineered solutions
"""

# https://en-gb.wordpress.org/plugins/browse/popular/ -> offline
# https://hansard.parliament.uk/search/Members?house=commons&currentFormerFilter=1 -> online

import requests
import bs4

result_wordpress = requests.get(
    "https://en-gb.wordpress.org/plugins/browse/popular/")

# Processing Offline
with open("wordpress.html", "w") as file_wordpress:
    file_wordpress.write(result_wordpress.text)

# Processing Online
result_hansard = requests.get(
    "https://hansard.parliament.uk/search/Members?house=commons&currentFormerFilter=1"
)

with open("hansard.html", "w") as file_hansard:
    file_hansard.write(result_hansard.text)
