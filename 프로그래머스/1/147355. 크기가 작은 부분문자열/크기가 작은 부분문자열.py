def solution(t, p):
    answer=[]
    answer2=[]
    for i in range(len(t)-len(p)+1):
        answer.append(t[i:i+len(p)])
    for b in answer:
        if int(b)<=int(p):
            answer2.append(b)
    return len(answer2)