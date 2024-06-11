def solution(my_string):
    answer = []
    for i,_ in enumerate(my_string):
        answer.append(my_string[i:])
    answer.sort()
    return answer