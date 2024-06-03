def solution(emergency):
    b=[]
    for e,a in enumerate(emergency):
        b.append(sorted(emergency,reverse=True).index(a)+1)
    return b