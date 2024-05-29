def solution(num_list, n):
    answer = []
    a=0
    b=[]
    for i in num_list:
        
        if a!=n:
            b.append(i)

        if a==n:
            a=0
            answer.append(b)
            b=[]
            b.append(i)
        a+=1
    answer.append(b)
    return answer