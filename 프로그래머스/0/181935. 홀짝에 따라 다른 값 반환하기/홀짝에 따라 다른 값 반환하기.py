def solution(n):
    a=[]
    if n%2==0:
        for i in range(n+1):
            if i%2==0:
                a.append(i**2)
    else:
        for i in range(n+1):
            if i%2==1:
                a.append(i)
    return sum(a)