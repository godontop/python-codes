# coding=utf-8

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = 'http://ip138.com'
_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:58.0) Gecko/20100101 Firefox/58.0'}

req = Request(url, headers=_headers)
page = urlopen(req).read()
soup = BeautifulSoup(page, 'lxml')
target = soup.find_all('iframe')
for iframe in target:
    src_page = urlopen(Request(iframe.attrs['src'], headers=_headers))
    iframe_soup = BeautifulSoup(src_page, 'lxml')
    print(iframe_soup.center.get_text())
