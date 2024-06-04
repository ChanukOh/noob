def solution(numlist, n):
    answer = []
    a=n
    b=n
    if n in numlist:
        answer.append(n)
    while len(answer)!=len(numlist):
        a+=1
        b-=1
        if a in numlist:
            answer.append(a)
        if b in numlist:
            answer.append(b)
            
            
    return answer