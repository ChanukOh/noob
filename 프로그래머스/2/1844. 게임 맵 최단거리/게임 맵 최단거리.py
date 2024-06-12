from collections import deque

def solution(grid):
    rows = len(grid)
    cols = len(grid[0])

    visited = [[False] * cols for _ in range(rows)] 
    queue = deque([(0, 0, 1)])  
    while queue:
        row, col, distance = queue.popleft()
        
        if row == rows - 1 and col == cols - 1:
            return distance  
        visited[row][col] = True

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1 and not visited[new_row][new_col]:
                queue.append((new_row, new_col, distance + 1))
                visited[new_row][new_col] = True
    
    return -1


