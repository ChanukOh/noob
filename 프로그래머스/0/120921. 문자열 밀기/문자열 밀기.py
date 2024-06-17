def solution(A, B):
    if A == B:
        return 0
    
    n = len(A)
    
    for i in range(n):
        if A == B:
            return i
        A = A[-1] + A[:-1] 
    return -1
