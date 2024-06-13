def solution(n,computers):
    answer=list(range(n))

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if computers[i][k]==1 and computers[k][j]==1:
                    computers[i][j]=1
                    answer[j]=answer[i]
    return len(set(answer))