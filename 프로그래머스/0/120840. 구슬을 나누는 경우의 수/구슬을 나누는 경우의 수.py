def solution(balls, share):
    a=balls
    b=1
    c=share
    d=1
    for i in range(share):
        b*=a
        a-=1
    for i in range(1,share):
        d*=c
        c-=1
    return b//d