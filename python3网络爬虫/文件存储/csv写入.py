import csv

with open('data.csv','w',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['id','name','age'])
    writer.writerow(['105080','sql',10])
    writer.writerow(['105081','java',11])
    writer.writerow(['105082','python',15])

with open('dataDir.csv','w',newline='') as F:   #在打开时添加参数newline可以删除空行
    fieldnames = ['id','name','age']
    writer = csv.DictWriter(F,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id':10001,'name':'Mike','age':15})
    writer.writerow({'id':10002,'name':'Joghn','age':15})
    writer.writerow({'id':10003,'name':'Jordan','age':15})

