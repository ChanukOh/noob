def solution(n):
    result=""
    while n>0:
        a=n%3
        result=str(a)+result
        n//=3
    b=0
    c=0
    for i in result:
        b += int(i) * (3 ** c)
        c += 1
    return b