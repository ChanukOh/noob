stu,prz=input().split()
score=input().split()
a=[]
for i in score:
    a.append(int(i))
a.sort()
print(a[-int(prz)])