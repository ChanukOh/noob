answer=0
for _ in range(int(input())):
    dic={}
    lis=[]
    c=0
    for i in str(input()):
        if lis!=[]:
            if lis[-1]!=i:
                dic[i]=dic.get(i,-1)+1
                c+=dic[i]
        else:
            dic[i]=dic.get(i,-1)+1
        lis.append(i)
    if c==0:
        answer+=1
print(answer)