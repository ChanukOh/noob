def solution(rank, attendance):
    x=[]
    
    for i,a in enumerate(rank):
        if attendance[i]==True:
            x.append(a)
    x.sort()
    a=rank.index(x[0])
    b=rank.index(x[1])
    c=rank.index(x[2])
    return (10000*a)+(100*b)+c