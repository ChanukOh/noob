def solution(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    memo = [0] * (n + 1)
    memo[0] = 1
    memo[1] = 1
    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
        memo[i] %= 1234567
    return memo[n]