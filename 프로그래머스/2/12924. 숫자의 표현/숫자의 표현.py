def solution(n):
    answer = 0
    start = 1
    
    while start <= n:
        sum = 0
        i = start
        while sum < n:
            sum += i
            i += 1
        if sum == n:
            answer += 1
        start += 1
    
    return answer