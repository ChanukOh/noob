def solution(num_list):
    answer=[]
    for i in num_list:
        a=0
        while i!=1:
            if i%2==0:
                i/=2
                a+=1
            else:
                i-=1
                i/=2
                a+=1
        answer.append(a)
    return sum(answer)