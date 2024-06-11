def solution(strArr):
    answer=[]
    for i,a in enumerate(strArr):
        if i%2==0:
            answer.append(a.lower())
        else:
            answer.append(a.upper())
    return answer