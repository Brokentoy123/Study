from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
import pymongo
from bs4 import BeautifulSoup as bs


webdriverPath="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
browser = webdriver.Chrome(executable_path=webdriverPath)
wait = WebDriverWait(browser,30)
KEYWORD = 'IPAD'
def index_page(page):
    """
    抓取索引页
    :param page:页码
    """
    print('正在爬取第'+str(page)+'页')
    try:
        url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
        browser.get(url)
        if page>1:
            input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR,"#mainsrp-pager div.form > input"))
            )
            submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR,'#mainsrp-pager div.form > span .btn J_Submit'))
            )
            input.clear()
            input.send_keys(page)
            submit.click()
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#mainsrp-pager li.item active > span'),str(page))
        )
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'.m-itemlist .items .item*'))
        )
        get_products()
    except TimeoutError :
        index_page(page)

def get_products():
    """
    提取商品数据
    """
    html = browser.page_source
    doc = bs(html,"html5lib")
    items = doc.find_all('#mainsrp-itemlist .items .item')
    for item in items:
        product = {
            'image' : item.find('.pic .img').attr('data-src'),
            'price' : item.find('.price').text(),
            'deal' : item.find('.deal-cnt').text(),
            'title' : item.find('.title').text(),
            'shop' : item.find('.shop').text(),
            'location' : item.find('.location').text()
        }
        print(product)
        save_to_mongo(product)

#保存到mongodb
MONGO_URL = 'localhost'
MONGO_DB = 'taobao'
MONGO_COLLECTION = 'products'
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]
def save_to_mongo(result):
    """
    保存至MONGODB
    """
    try:
        if db[MONGO_COLLECTION].insert(result):
            print("存储到mongoDB成功")
    except Exception:
        print("存储到mongoDB失败")

#遍历每一页
MAX_PAGE = 100
def main():
    """
    遍历每一页
    """
    for i in range(1,MAX_PAGE+1):
        index_page(i)

if __name__ == "__main__":
    main()
