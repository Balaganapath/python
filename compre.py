def fact(a):
    if a==1:
        return 1
    return a*fact(a-1)

a=[ fact(i)  for i in range(11,20)]
print(a)