def solution(k, score):
    answer=[]
    answer2=[]
    for i in score:
        if len(answer)<k:
            answer.append(i)
        else:
            if i>min(answer):
                answer.sort()
                answer[0]=i
        answer2.append(min(answer))
    return answer2