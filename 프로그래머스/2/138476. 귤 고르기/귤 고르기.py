def solution(k, tangerine):
    dic={}
    for i in tangerine:
        dic[i]=dic.get(i,0)+1
    answer=sorted(list(dic.values()),reverse=True)
    count=0
    ind=0
    while k>0:
        k-=answer[ind]
        count+=1
        ind+=1
    return count