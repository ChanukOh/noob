b='abcdefghijklmnopqrstuvwxyz'
dic={}
for i in b:
    dic[i]=-1
a=str(input())
for n,j in enumerate(a):
    if dic[j]==-1:
        dic[j]=n
a=[]
for i in b:
    a.append(str(dic[i]))
print(' '.join(a))