def solution(d, budget):
    a=budget
    answer = []
    for i in sorted(d):
        if a>=i:
            answer.append(i)
            a-=i
    return len(answer)