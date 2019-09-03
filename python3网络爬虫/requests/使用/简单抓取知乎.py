import requests
import re


headers = {
    'Cookie':'_zap=e4447a01-d9e6-45da-bc3d-3387d717bfcd; d_c0="AJAjIA4W5g-PTmfacy75xnSKYtn6K2vG9Y0=|1565918858"; _xsrf=fyweZlQEGY6yRJG8mOcv6KoKJQn1Crit; capsion_ticket="2|1:0|10:1567293623|14:capsion_ticket|44:ZTMxZWNlOTZhMmQwNGYxZGExM2ZkMzJiMGUzZDQ2MmE=|fa000a888a95355c0b2de6ffe618a86b67f0262e90c3cfdc7bc456c087d3ae2b"; z_c0="2|1:0|10:1567293635|4:z_c0|92:Mi4xTGpTM0F3QUFBQUFBa0NNZ0RoYm1EeVlBQUFCZ0FsVk53MDVZWGdCUkJKeFlGby1Wazh2em1ZS0lYa3BsQTZSTFRR|6f3a51041db661f2ec33fffc9d42ebd4e29200232997e370345b6b888687c2bb"; tst=r; q_c1=43d3c40b1c2d45c28c61f24ea8584e08|1567294924000|1567294924000; tgw_l7_route=f2979fdd289e2265b2f12e4f4a478330',
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
r = requests.get("https://www.zhihu.com/explore",headers=headers)
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)
titles = re.findall(pattern,r.text)
print(titles)