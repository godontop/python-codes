# coding=utf-8

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = 'https://www.whatismybrowser.com/'
_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:58.0) Gecko/20100101 Firefox/58.0'}

req = Request(url, headers=_headers)
page = urlopen(req).read()
soup = BeautifulSoup(page, 'lxml')
target_div = soup.find_all('div', class_="user-agent")[0].a.get_text()
print(target_div)
