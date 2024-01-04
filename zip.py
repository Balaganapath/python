a=[3,2,1]
b=[8,5,5]
c=[1,2,3]
out=[]
for i ,j,k in zip(a,b,c):
    out=out+[i]+[j]+[k]
print(out)    