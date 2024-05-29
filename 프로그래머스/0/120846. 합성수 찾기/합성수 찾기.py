def is_composite(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True
    return False

def solution(n):
    count = 0
    for num in range(1,n+1):
        if is_composite(num):
            count += 1
    return count

print(solution(10))  