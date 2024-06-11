def solution(numLog):
    answer=[]
    j=0
    for i in numLog:
        if j-i==0:
            pass
        if j-i==-1:
            answer.append("w")
        if j-i==1:
            answer.append("s")
        if j-i==10:
            answer.append("a")
        if j-i==-10:
            answer.append("d")
        j=i
    return ''.join(answer)