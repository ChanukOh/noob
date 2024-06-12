def solution(n, computers):
    def dfs(computers, visited, node):
        stack = [node]
        while stack:
            current = stack.pop()
            if not visited[current]:
                visited[current] = True
                for idx, connected in enumerate(computers[current]):
                    if connected and not visited[idx]:
                        stack.append(idx)

    num_networks = 0
    visited = [False] * n

    for node in range(n):
        if not visited[node]:
            dfs(computers, visited, node)
            num_networks += 1

    return num_networks