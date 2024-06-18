def solution(numbers):
    dic={}
    for i in range(10):
        dic[i]=i
    for j in numbers:
        dic[j]=0
    
    return sum(dic.values())