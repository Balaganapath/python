a=int(input('enter the value:-'))
b=int (input('enter the value:-'))
option=eval(input('enter arithematic :-'))
match option:
    case 1:
        d=a+b
        print(d)
    case 2:
        d=a*b
        print(d)
    case 3:
        d=a-b
        print(d)
print(d)