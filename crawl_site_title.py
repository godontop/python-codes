# coding=utf-8

'''
urllib的默认User-Agent是Python-urllib/x.y，其中x、y分别对应sys.version_info.major
和sys.version_info.minor，即Python的主版本号和次版本号。
因为很多网站都禁止Python爬虫，所以需要将爬虫程序的User-Agent伪装成常规浏览器。
https://www.baidu.com 和https://www.liaoxuefeng.com就禁止了Python爬虫，在没有伪装
用户代理时https://www.baidu.com返回的是另一个版本，而https://wwww.liaoxuefeng.com
则直接返回503的错误。
'''

from urllib.request import urlopen, Request

from bs4 import BeautifulSoup

url = 'https://www.baidu.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

req = Request(url, headers=headers)
page = urlopen(req).read()
soup = BeautifulSoup(page, 'lxml')
print(soup.title.contents[0])
