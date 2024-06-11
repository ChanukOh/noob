def solution(my_strings, parts):
    answer=[]
    for a,b in enumerate(parts):
        answer.append(my_strings[a][b[0]:b[1]+1])
    return ''.join(answer)