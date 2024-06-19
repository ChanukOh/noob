def solution(s, n):
    alpha='abcdefghijklmnopqrstuvwxyz'
    alphabig=alpha.upper()
    answer=[]
    for i in s:
        if i in alpha:
            i=alpha[(alpha.index(i)+n)%26]
            
        elif i in alphabig:
            i=alphabig[(alphabig.index(i)+n)%26]
        answer.append(i)
    return ''.join(answer)