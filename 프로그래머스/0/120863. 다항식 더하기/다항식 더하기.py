def solution(polynomial):
    a = 0
    c = []
    answer = polynomial.split()
    for i in answer:
        if 'x' in i:
            b = i.replace('x', '')
            if b == "+" or b == "":
                b = '1'
            elif b == "-":
                b = '-1'
            a += int(b)
        else:
            c.append(i)
    d = [f"{a}x"]
    d = d + c
    e = ' '.join(d)
    while e and not (e[-1].isdigit() or e[-1] == 'x'):
        e = e.rstrip('+- ')
        
    x=0
    y='+'
    sent1=e.split(" ")
    for i in sent1:
        if i=="+":
            y='+'
        if i=="-":
            y='-'
        if i.isdigit() and y=="+":
            x+=int(i)
            y=''
        if i.isdigit() and y=="-":
            x-=int(i)
            y=''
    if a==1:
        return f"x" if x==0 else f"x + {x}"
    elif a==0:
        return f"" if x==0 else f"{x}"
    return f"{a}x" if x==0 else f"{a}x + {x}"
