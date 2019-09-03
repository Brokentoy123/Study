import socket
import urllib.request
import urllib.error


try:
    respons = urllib.request.urlopen('https://www.baodu.com',timeout=0.01)
except urllib.error.URLError as e:
    print(type(e))
    if isinstance(e.reason,socket.timeout):
        print("TIME OUT")
        
