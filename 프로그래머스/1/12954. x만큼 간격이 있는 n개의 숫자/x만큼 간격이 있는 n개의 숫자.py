def solution(x, n):
    if x==0:
        answer=[]
        for i in range(n):
            answer.append(0)
        return answer
    return list(range(x,x*n+x,x))