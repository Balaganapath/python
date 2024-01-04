class emploee:
    company='janasena'
    ceo='pa1kalyan'

    def insert_member(obj,name,salary,eid):
        obj.name=name
        obj.salary=salary
        obj.eid=eid
gana=emploee()    
bala=emploee()
emploee.insert_member(gana,'gana',4700,2024)  
emploee.insert_member(bala,'bala',4700,2023)  
