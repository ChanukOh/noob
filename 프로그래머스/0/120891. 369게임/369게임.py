def solution(order):
    a=0
    for i in str(order):
        if int(i)==0:
            continue
        if int(i)%3==0:
            a+=1
    return a