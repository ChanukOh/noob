def solution(start, end_num):
    a=start
    b=[]
    for i in range(end_num,start+1):
        b.append(a)
        a-=1
    return b