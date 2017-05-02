#!/usr/bin/env python2.7

import re
import requests

from lxml import html

from bs4 import BeautifulSoup


from selenium import webdriver

URL = "http://docs.southbendin.gov/weblink/0/doc/27986/Page1.aspx"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
    'Content-Type': 'text/html',
}

site = requests.get(URL, headers=headers)

soup = BeautifulSoup(site.text, 'html.parser')


tree = html.fromstring(site.content)
thing = tree.xpath('//*[@id="PageA"]/img')

#get how many pages are in the pdf
regex = "PageNumberToolbarCount\">([0-9]+)"
pageNums = re.findall(regex, site.text)

#get pdfID -- can be used to find the urls of the images of the pages
regex2 = "/doc/([0-9]+)/"
pdfID = re.findall(regex2, URL)


start = "http://docs.southbendin.gov/WebLink/PageImageData.aspx?scale=3752&dID="
middle = "&pageNum="
end = "&ann=1&r=&search=&ro=0"

images = []
for page in range (1, int(pageNums[0]) + 1):
    image = start + pdfID[0] + middle + str(page) + end
    images.append(image)
    print image
#print images

#print site.text
#print thing



#driver = webdriver.Firefox()
#driver.get("http://docs.southbendin.gov/weblink/0/doc/27986/Page1.aspx")
#print driver.title
