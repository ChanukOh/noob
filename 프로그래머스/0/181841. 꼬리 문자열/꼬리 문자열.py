def solution(str_list, ex):
    answer = []
    for i in str_list:
        if ex in i:
            pass
        else:
            answer.append(i)
    return ''.join(answer)