a=input()
b=[]
for i in a:
    b.append(int(i))
b.sort(reverse=True)
c=''
for i in b:
    c+=str(i)
print(c)