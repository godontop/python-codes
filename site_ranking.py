# coding=utf-8

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

site = input("Enter a site, such as example.com: ")
url = 'https://www.alexa.com/siteinfo/{}'.format(site)
_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:58.0) Gecko/20100101 Firefox/58.0'}

req = Request(url, headers=_headers)
page = urlopen(req).read()
soup = BeautifulSoup(page, 'lxml')
target_title = soup.find_all(
    'h4', class_="metrics-title")[0].contents[0]
ranking = soup.find_all(
    'strong', class_="metrics-data align-vmiddle")[0].get_text()
print(target_title.strip())
print(ranking.strip())
