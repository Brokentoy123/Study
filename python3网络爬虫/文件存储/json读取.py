import json
str = """[{
    "name":"Bob",
    "gender":"male",
    "birthday":"1992-10-18"
},{
    "name":"Selina",
    "gender":"female",
    "birthday":"1995-10-18"
}
]"""
data = json.loads(str)
print(data[0])
print(data[0]['name'])
print(data[0].get('name'))