def fact():
    a=int(input('enter a value:-'))
    out=1
    for i in range(1,a+1):
        out*=a
        a-=1
    print(out)
fact() 