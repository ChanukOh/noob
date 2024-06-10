def solution(array, commands):
    a=[]
    for i in commands:
        b=array[i[0]-1:i[1]]
        b.sort()
        a.append(b[i[2]-1])
    return a