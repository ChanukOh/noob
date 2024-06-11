def solution(myString, pat):
    answer = myString.replace("A","b").replace("B",'a').swapcase()
    return 1 if pat in answer else 0