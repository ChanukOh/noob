def solution(numbers, n):
    a=0
    for i in numbers:
        a+=i
        if a>n:
            return a
            
    return 0