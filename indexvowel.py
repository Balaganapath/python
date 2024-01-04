def index_vowel(a):
    out=[]
    i=0
    for i in range(0,len(a)):
        if  a[i] in 'aeiouAEIOU':
            out=out+[i]
            i=i+1
    return out
out=index_vowel('focus what you have')
print(out)             
  