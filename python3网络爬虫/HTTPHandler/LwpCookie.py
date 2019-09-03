import http.cookiejar,urllib.request



fileName = 'cookie.txt'

cookie = http.cookiejar.LWPCookieJar(fileName)

handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True,ignore_expires=True)
cookie.load('cookie.txt',ignore_discard=True,ignore_expires=True)

print(response.read().decode('utf-8'))