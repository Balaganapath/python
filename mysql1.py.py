import pymysql

conn=pymysql.connect(user='root',password='root',port=3306,database='pythonmysql')
cursor=conn.cursor()
query='''create table ceo(
    id int primary key,
    name varchar(100),
    mobile bigint unique,
    balance bigint
);'''
cursor.execute(query)