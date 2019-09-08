import socks
import socket
from urllib.error import URLError
from urllib import request


socks.set_default_proxy(socks.SOCKS5,'127.0.0.1',980)
socket.socket = socks.socksocket
try:
    response = request.urlopen('http://httpbin.org/get')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)