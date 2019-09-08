from urllib.error import URLError
from urllib.request import ProxyHandler,build_opener

proxy='127.0.0.1:980'
proxy_handler = ProxyHandler({
    'http':'http://'+proxy,
    'https':'https://'+proxy
})
opener = build_opener(proxy_handler)
try:
    response = opener.open('https://httpbin.org/get')
    print(response.read().decode('utf-8'))
except URLError as e:
    pprint(e.reason)
