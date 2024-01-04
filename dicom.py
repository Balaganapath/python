seats=int(input ('conform no of seats:-'))
option=int(input('select the type of class:-'))
match option:
    case 1:
        print("diamond")
        amt=seats*200      #match case example book seats
    case 2:
        print("gold")
        amt=seats*150
    case 3:
        print("silver")        
        amt=seats*100
    case _:
        print("invalid")
        amt=None    
print(amt)        