def solution(num, total):
    a=0
    while True:
        start=total-num+a
        end=total+a
        b=range(start,end)
        if sum(range(start,end))==total:
            return list(range(start,end))
        else:
            if sum(range(start,end))<total:
                a+=1
            else:
                a-=4