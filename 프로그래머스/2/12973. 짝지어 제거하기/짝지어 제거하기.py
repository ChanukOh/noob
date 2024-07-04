def solution(s):
    a = []
    for i in s:
        if a and a[-1] == i:
            a.pop()
        else:
            a.append(i)
    
    return 1 if not a else 0