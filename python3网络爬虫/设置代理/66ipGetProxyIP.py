import requests
from bs4 import BeautifulSoup
from redis import Redis
from urllib.parse import urlencode
import random
import re
from selenium import webdriver
import time


url = 'http://www.66ip.cn/nmtq.php?'

#1.url分析
def setUrl(num):
    params={
        'getnum':num,
        'isp':0,
        'anonymoustype':4,
        'start':'',
        'ports':'',
        'export':'',
        'ipaddress':'',
        'area':0,
        'proxytype':2,
        'api':'66ip'
    }
    return params
headers = {
    'Cookie': 'Hm_lvt_1761fabf3c988e7f04bec51acd4073f4=1567921272; Hm_lpvt_1761fabf3c988e7f04bec51acd4073f4=1567922314',
    'Host': 'www.66ip.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
url = url + urlencode(setUrl(random.randint(1,31)))
web = webdriver.Chrome()
web.get(url)
time.sleep(1)
response = web.page_source
print(response)
ips = re.findall('(\w+\.\w+\.\w+\.\w+):(\w+)<br>',response,re.S)
print("ips:",ips)
# print("ports:",ports)

#2.获取ip地址池
