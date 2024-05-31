def solution(my_string, n):
    return ''.join(i for i in my_string for b in range(n))