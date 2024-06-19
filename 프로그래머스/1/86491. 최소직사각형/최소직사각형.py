def solution(sizes):
    answer1=0
    answer2=0
    for xy in sizes:
        xy.sort()
        x,y=xy[0],xy[1]
        if answer1<x:
            answer1=x
        if answer2<y:
            answer2=y
    return answer1*answer2