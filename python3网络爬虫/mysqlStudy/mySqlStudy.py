import pymysql

db = pymysql.connect(host='localhost',user='root',password='shiqinghua',port=3306)
cursor = db.cursor()
sql='use spiders;'
cursor.execute(sql)
sql="create table if not exists students (id varchar(255) not null,name varchar(255) not null,age int not null,primary key(id));"
cursor.execute(sql)
db.close()