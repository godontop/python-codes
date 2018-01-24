# coding=utf-8

from urllib.request import urlopen, Request

from bs4 import BeautifulSoup

url = 'https://whatismyipaddress.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

req = Request(url, headers=headers)
page = urlopen(req).read()
soup = BeautifulSoup(page, 'lxml')
print(soup.find_all('div', style="text-align:center;font-size:26px;padding-top:0px;color:#000;")
      [0].get_text(), end=' ')
print(soup.find_all(
    'div', style="text-align:center;padding-top:4px;")[0].get_text())
print(soup.find_all('div', style="text-align:center;color:#000;font-weight:bold;")
      [0].get_text(), end=' ')
print(soup.table.get_text())
