import http.cookiejar,urllib.request

fileName = 'cookies.txt'
cookie = http.cookiejar.MozillaCookieJar(fileName)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True,ignore_expires=True)