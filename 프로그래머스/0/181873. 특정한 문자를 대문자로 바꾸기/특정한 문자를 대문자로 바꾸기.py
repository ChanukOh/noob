def solution(my_string, alp):
    bigalp=alp.swapcase()
    answer=my_string.replace(f"{alp}",f"{bigalp}")
    return answer