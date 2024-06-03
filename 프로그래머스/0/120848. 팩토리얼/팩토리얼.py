def solution(n):
    a=[]
    for i in range(n):
        v=1
        a.append(i+1)
        for b in range(len(a)):
            v*=a[b]
            if v==n:
                return i+1
            if v>n:
                return i