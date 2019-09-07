import requests


url = 'http://localhost:8050/render.har?url=https://www.jd.com&wait=5'
response = requests.get(url)
print(response.content)