def solution(dots):
    c=[]
    d=[]
    for a,b in dots:
        c.append(a)
        d.append(b)
    c=list(set(c))
    d=list(set(d))

    return (max(c)-min(c))*(max(d)-min(d))