
def solution(slice, n):
    for i in range(n+1):
        if slice*i//n<=0:
            pass
        if slice*i//n>=1:
            return i