def solution(strArr):
    dic={}
    maxk=0
    maxv=0
    for i in strArr:
        dic[len(i)]=dic.get(len(i),0)+1
    for key,value in dic.items():
        if maxv<value:
                maxk,maxv=key,value
    return maxv