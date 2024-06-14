def solution(numlist):
    def arr(x):
        for i,a in enumerate(x):
            if a<50 and a%2==1:
                x[i]=a*2+1
            elif a>50 and a%2==0:
                x[i]=a/2
        return x
    z=0
    prev=numlist[:]
    current=arr(numlist)
    while prev!=current:
        prev=current[:]
        current=arr(numlist)
        z+=1
    return z