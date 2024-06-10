import sys

sys.setrecursionlimit(10**6)

def dfs(wmap, row, col, visited):
    if row < 0 or col < 0 or row >= len(wmap) or col >= len(wmap[0]) or wmap[row][col] == 0 or visited[row][col]:
        return
    visited[row][col] = True  

    for dr in range(-1, 2):
        for dc in range(-1, 2):
            dfs(wmap, row + dr, col + dc, visited)

def count_connected_regions(wmap):
    num_regions = 0 
    visited = [[False] * len(wmap[0]) for _ in range(len(wmap))]  

    for i in range(len(wmap)):
        for j in range(len(wmap[0])):
            if wmap[i][j] == 1 and not visited[i][j]:  
                dfs(wmap, i, j, visited)
                num_regions += 1

    return num_regions

while True:
    try:
        n = list(map(int, input().split()))
        if n[0] == 0:
            break
        worldmap = []
        for i in range(n[1]):
            worldmap.append(list(map(int, input().split())))
        print(count_connected_regions(worldmap))
    except EOFError:
        break