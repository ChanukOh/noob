def solution(left, right):
    plus=[]
    minus=[]
    for i in range(left,right+1):
        a=[i]
        for j in range(1,i+1):
            if i%j==0:
                a.append(j)
        if len(a)%2==1:
            plus.append(i)
        else:
            minus.append(i)
    return sum(plus)-sum(minus)