def solution(sides):
    a=[]
    for i in range(1,max(sides)+min(sides)):
        if min(sides)+i>max(sides):
            a.append(i)
        elif i>=max(sides) and max(sides)+min(sides)>i:
            a.append(i)
    return len(a)