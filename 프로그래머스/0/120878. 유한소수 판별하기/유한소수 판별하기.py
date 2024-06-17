def solution(a, b):
    for i in range(1,b):
        if a%i==0 and b%i==0:
            a/=i
            b/=i
    while b%2==0:
        b/=2
    while b%5==0:
        b/=5
    return 1 if b==1 else 2