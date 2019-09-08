from selenium import webdriver


proxy = '127.0.0.1:980'
chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument('--proxy-server=http://' + proxy)
browser = webdriver.Chrome(chrome_options=chrome_option)
browser.get('http://httpbin.org/get')
