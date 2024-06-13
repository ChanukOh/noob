def solution(board, k):
    c=[]
    for i,a in enumerate(board):
        for j,b in enumerate(board[i]):
            if i+j<=k:
                c.append(board[i][j])
    return sum(c)