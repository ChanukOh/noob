def solution(array):
    a=0
    for i in array:
        for b in str(i):
            if b=="7":
                a+=1
    return a