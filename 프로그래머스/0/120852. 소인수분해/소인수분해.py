def solution(n):
    a=[]
    for i in range(2,n+1):
        
        if n%i==0:
            a.append(i)
        while n%i==0:
            n//=i
            
    return a