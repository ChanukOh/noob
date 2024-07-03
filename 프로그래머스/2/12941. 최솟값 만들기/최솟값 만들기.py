def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    a,b=len(A),len(B)
    for i in range(min([a,b])):
        answer+=A[i]*B[i]

    return answer