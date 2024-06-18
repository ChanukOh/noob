def solution(n):
    answer = [int(i) for i in str(n)]
    a=map(str,sorted(answer,reverse=True))

    return int(''.join(a))