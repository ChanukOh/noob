def solution(s):
    a=[]
    check=1
    for i in s:
        if check==1:
            a.append(i.upper())
            check=0
        else:
            a.append(i.lower())
        if a[-1]==' ':
            check=1
    return ''.join(a)