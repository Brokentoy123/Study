import requests
from bs4 import BeautifulSoup
from redis import Redis


url = 'http://www.66ip.cn/nm.html'

#1.模拟填写表单
html = requests.get(url)
print(html)
#2.获取ip地址池
