import random
def solution(numbers):
    a=[]

    for i in range(len(numbers)*50):
        e,f,g=random.sample(numbers,3)
        b=e+f
        c=f+g
        d=e+g

        a.append(b)
        a.append(c)
        a.append(d)
    return sorted(list(set(a)))