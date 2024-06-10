def solution(str1, str2):
    c=[]
    for i,a in enumerate(str1):
        c.append(a)
        c.append(str2[i])
    return ''.join(c)