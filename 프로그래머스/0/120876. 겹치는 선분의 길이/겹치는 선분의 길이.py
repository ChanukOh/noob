def solution(lines):
    b=[]
    answer=[]
    for c,d in lines:
        for i in range(c,d):
            if i in b:
                answer.append(i)
            else:
                b.append(i)
    return len(set(answer))