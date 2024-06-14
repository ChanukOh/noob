def solution(n):
    a=[]
    for i in range(n*3):
        if i%3!=0 and "3" not in str(i):
            a.append(i)
        
    return a[n-1]