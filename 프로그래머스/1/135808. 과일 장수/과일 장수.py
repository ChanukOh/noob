def solution(k, m, score):
    answer = []
    score.sort(reverse=True)
    cash=0
    temp_list = []
    for idx, val in enumerate(score):
        temp_list.append(val)
        if (idx + 1) % m == 0:
            answer.append(temp_list)
            temp_list = []
    for i in answer:
        cash+=i[-1]*len(i)
    return cash