def solution(l, r):
    answer=[]
    for i in range(l,r+1):
        a=str(i)
        if "1" in a or "2" in a or "3" in a or "4" in a or "6" in a or "7" in a or "8" in a or "9" in a:
            pass
        else:
            answer.append(i)
    return answer if len(answer)!=0 else [-1]