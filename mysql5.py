import pymysql

conn=pymysql.connect(user='root',password='root',port=3306,database='pythonmysql')
cursor=conn.cursor()
'''def creater_table():
    try:
        query="create table ceo(
        id int primary key,
        name varchar(100),
        mobile bigint unique,
        balance bigint
        );"
        cursor.execute(query)
    except pymysql.err.operationalError as e:
        print(f'{e}')'''
'''def insert_record():
    query='insert into ceo(id,name,mobile,balance) values(1,"bala",2564123,2561651)'            

    cursor.execute(query)
    conn.commit()
insert_record() '''

'''def get_record():
    query='select *from ceo'
    cursor.execute(query)
    record=cursor.fetchall()
    for i in record:
    
        print(i)
get_record() ''' 

'''def insert_dynamic(id,name,mobile,balance):
    record=(id,name,mobile,balance)
    query='insert into ceo(id,name,mobile,balance) values(%d,%s,%d,%d)'%record
    cursor.execute(query,record)
    conn.commit()'''

def drop_record(id):
    query=f'delete from ceo where id ={id}'
    cursor.execute(query)
    conn.commit()
    print('record removed')    