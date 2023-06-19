--using https://oxylabs.io/blog/python-web-scraping tutorial 
--with a website of my choosing

import requests

--parsing a friends website (soccer blog for Italian team focused on US audience)
url = 'https://www.violanation.com/'
response = requests.get(url)

from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title)
--result
<title>Viola Nation, a Fiorentina community</title>

blog_titles = soup.findAll(['h3','h4','h5'])
for title in blog_titles:
    print(title.text)
--result lists large number of blog titles

blog_titles = soup.select('h3, h4, h5:not(:-soup-contains("Chloe"))')
for title in blog_titles:
    print(title.text)
--result lists same titles from above but without an opion article written by a Chloe

--using lmxl to parse this website
--website is small, so html might not be optimally designed
--this could cause problems for lmxl
# After response = requests.get()
from lxml import html
tree = html.fromstring(response.text)

blog_titles = tree.xpath('//h3 | //h4 | //h5[not(contains(text(), "Fiorentina"))]')
for title in blog_titles:
    print(title.text)
--result returns a bunch of 'None's

