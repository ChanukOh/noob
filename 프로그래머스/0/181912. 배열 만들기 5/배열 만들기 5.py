def solution(intStrs, k, s, l):
    a=[]
    b=[]
    for i in intStrs:
        a.append(i[s:s+l])
    a=list(map(int,a))
    for i in a:
        if i>k:
            b.append(i)
    return b