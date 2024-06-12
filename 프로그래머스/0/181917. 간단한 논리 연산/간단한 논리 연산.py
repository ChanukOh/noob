def solution(x1, x2, x3, x4):
    x5=True
    x6=False
    if x1==True or x2==True:
        x5=True
    else:
        x5=False
    if x3==True or x4==True:
        x6=True
    else:
        x6=False
    if x5==True and x6==True:
        return True
    else:
        return False