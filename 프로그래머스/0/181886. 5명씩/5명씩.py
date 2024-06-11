def solution(names):
    answer = []
    for i,a in enumerate(names):
        if i%5==0:
            answer.append(a)
    return answer