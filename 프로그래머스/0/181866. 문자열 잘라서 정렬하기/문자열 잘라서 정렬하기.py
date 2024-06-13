def solution(myString):
    a=sorted(myString.split('x'))
    b=[]
    for i in a:
        if i!='':
            b.append(i)
    return b