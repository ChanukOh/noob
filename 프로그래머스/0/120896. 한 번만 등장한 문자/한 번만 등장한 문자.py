def solution(s):
    a={}
    d=[]
    for i in s:
        a[i]=a.get(i,0)+1
    for b,c in a.items():
        if c==1:
            d.append(b)
    if len(d)!=0:
        return "".join(sorted(d))
    return