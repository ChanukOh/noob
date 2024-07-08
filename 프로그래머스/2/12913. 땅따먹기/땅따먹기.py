def solution(land):
    N = len(land)
    dp = [[0] * 4 for _ in range(N)]
    dp[0] = land[0]
    for i in range(1, N):
        for j in range(4):
            max_previous = 0
            for k in range(4):
                if j != k:
                    max_previous = max(max_previous, dp[i-1][k])
            dp[i][j] = land[i][j] + max_previous
    answer = max(dp[N-1])
    
    return answer