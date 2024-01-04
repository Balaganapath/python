'''import csv
with open('mca.csv','w',newline='') as csvfile:
    data=csv.writer(csvfile)
    data.writerow(['id','name','mobile','email'])
    data2=[
        [1,'jos',124578964,'jas@gmail.com'],

        [2,'hello',123657890,'helo@gmail.com'],

        [4,'boys',451278963,'boy@gmail.com']
    ]
    data.writerow(data2)'''
    
import csv
'''with open('mca.csv','r') as csvfile:
        data = csv.reader(csvfile)
        for i in data:
            print(i)'''

'''with open('mca1.csv','w',newline='') as csvfile:
    fieldname =['id','name','mobile','email']
    data=csv.DictWriter(csvfile,fieldname)
    data.writeheader()
    row=[
        {'id':1,'name':'bala','mobile':8314789456,'email':'bala@gmail.com'},
        {'id':5,'name':'ganapathi','mobile':8374135085,'email':'gana@gmail.com'}
    ]
    data.writerows(row)'''            

with open('mca1.csv','r') as csvfile:
    data=csv.DictReader(csvfile)
    for row in data:
        print(row['name'])