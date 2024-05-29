def solution(num, k):
    answer = 1
    for i in str(num):
        if i==str(k):
            return answer
        else:
            answer+=1
    
    return -1