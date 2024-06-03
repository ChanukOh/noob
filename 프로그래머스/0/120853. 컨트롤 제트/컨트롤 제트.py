def solution(s):
    a=0
    b=0
    for i in s.split():
        c=1
        if "-" in i:
            c=-1
            i=i[1:]
        if i.isdigit():
            b=a
            a+=int(i)*c
            
        if i=="Z":
            a=b
        
    return a