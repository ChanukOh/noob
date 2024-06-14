def solution(my_string):
    answer = []
    ms2='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in ms2:
        answer.append(my_string.count(i))
    for i in ms2.lower():
        answer.append(my_string.count(i))
    return answer