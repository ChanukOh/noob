def solution(array, n):
    a=n
    b=n
    c=0
    d=0
    for i in range(-n,max(array)):
        if a in array:
            c=1
        if b in array:
            d=1
        if c==1:
            return a
        if d==1:
            if c==0:
                return b
        a-=1
        b+=1