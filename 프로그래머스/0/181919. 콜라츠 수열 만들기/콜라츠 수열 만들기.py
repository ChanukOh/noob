
def solution(n,lis=[]):
    if n%2==0:
        lis.append(n)
        return solution(n//2,lis)
    elif n==1:
        lis.append(n)
        return lis
    else: 
        lis.append(n)
        return solution(3*n+1,lis)