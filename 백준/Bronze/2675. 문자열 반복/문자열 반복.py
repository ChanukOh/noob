for i in range(int(input())):
    a,b=str(input()).split()
    c=[]
    for j in b:
        for i in range(int(a)):
            c.append(j)
    print(''.join(c))