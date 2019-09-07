import requests


url = 'http://localhost:8050/render.png?url=https://www.jd.com&wait=5&width=1000&height=700'
response = requests.get(url)
with open("renderPng.png",'wb') as p:
    p.write(response.content)
