import requests
import re
import json
import time

def get_one_page(url):
    headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }
    
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        #print(response.text)
        return response.text
    return None

def parse_one_page(html):
    # parttern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?board-img.*?src="(.*?)".*?name.*?<a'
    #                     +'.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?'
    #                     +'>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',re.S)

    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern,html)
    for item in items:
        yield {
            'index':item[0],
            'image':item[1],
            'title':item[2].strip(),
            'actor':item[3].strip()[3:] if len(item[3]) > 3 else '',
            'time':item[4].strip()[5:] if len(item[4]) > 5 else '',
            'score':item[5].strip()+item[6].strip()
        }

def write_to_file(content):
    with open("result.text",'a',encoding='utf8') as f:
        #print(type(json.dumps(content)))
        f.write(json.dumps(content,ensure_ascii=False)+'\n')

def main(offset):
    url = 'https://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):  
        write_to_file(item)

if __name__ == "__main__":
    for i in  range(10):
        main(offset=i * 10)
