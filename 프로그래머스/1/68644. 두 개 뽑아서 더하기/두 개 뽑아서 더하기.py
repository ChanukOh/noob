import random
def solution(numbers):
    a=[]
    d=range(len(numbers)*10)
    for i in range(len(numbers)):
        for c in d:
            e,f=random.sample(numbers,2)
            b=e+f
            if b in a:
                pass
            else:
                a.append(b)
    return sorted(a)