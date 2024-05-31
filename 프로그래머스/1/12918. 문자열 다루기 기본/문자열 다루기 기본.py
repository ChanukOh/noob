def solution(s):
    a=[]
    for i in s:
        if i.isdigit()==False:
            return False
    if len(s)==4 or len(s)==6:
            return True
    else:
        return False