import requests
from urllib.parse import quote


lua = """
function main(splash)
  return 'Hello'
end
"""

url = "http://localhost:8050/execute?lua_source=" + quote(lua)
response = requests.get(url)
print(response.content)