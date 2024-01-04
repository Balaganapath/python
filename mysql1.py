import pymysql

conn=pymysql.connect(user='root',password='root',port=3306,host='localhost')
cursor=conn.cursor()
query = 'create database pythonmysql'
cursor.execute(query)