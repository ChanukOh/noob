def solution(a, b, c, d):
    abcd=[a,b,c,d]
    setd=list(set(abcd))
    if len(setd)==1:
        return a*1111
    elif len(setd)==2:
        if abcd.count(a)==2:
            abcd.sort()
            return (abcd[-1]+abcd[0])*(abs(abcd[-1]-abcd[0]))
        elif abcd.count(b)==1:
            return (10*a+b)*(10*a+b)
        elif abcd.count(c)==1:
            return (10*b+c)*(10*b+c)
        elif abcd.count(d)==1:
            return (10*b+d)*(10*b+d)
        elif abcd.count(a)==1:
            return (10*b+a)*(10*b+a)
        
    elif len(setd)==3:
        for i,a in enumerate(abcd):
            if abcd.count(a)==2:
                abcd.pop(i)
                abcd.pop(abcd.index(a))
                return abcd[0]*abcd[1]
    else:       
        return min(abcd)