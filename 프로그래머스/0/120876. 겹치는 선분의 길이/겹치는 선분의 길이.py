def solution(lines):
    bs=[]
    answer=[]
    for c,d in lines:
        for i in range(c,d):
            if i in bs:
                answer.append(i)
            else:
                bs.append(i)
    return len(set(answer))