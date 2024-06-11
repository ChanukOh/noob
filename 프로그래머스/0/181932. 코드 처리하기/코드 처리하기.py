def solution(code):
    mode=0
    b=[]
    for i,a in enumerate(code):
        if mode==0:
            if a=="1":
                mode=1
            elif i%2==0:
                b.append(a)
        elif mode==1:
            if a=="1":
                mode=0
            elif i%2==1:
                b.append(a)
    return ''.join(b) if len(b)!=0 else 'EMPTY'