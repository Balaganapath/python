def sum(st,end):
    if st == end:
        return st
    return st + sum(st+1,end)
out=sum(1,10)
print(out)         