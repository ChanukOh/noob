def solution(board):
    n = len(board)
    safe_count = 0
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0: 
                count_mines = 0
                
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1:
                            count_mines += 1

                if count_mines == 0:
                    safe_count += 1
    
    return safe_count
