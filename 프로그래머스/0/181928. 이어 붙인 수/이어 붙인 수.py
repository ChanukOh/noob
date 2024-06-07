def solution(num_list):
    a=[]
    b=[]
    for i in num_list:
        if i%2==0:
            a.append(i)
        else:
            b.append(i)
    c=''
    d=''
    for i in a:
        c+=str(i)
    for i in b:
        d+=str(i)
    return int(c)+int(d)