def solution(n, m, section):
    answer = 0
    checked = set()
    for i in section:
        if i not in checked:
            for j in range(m):
                checked.add(i + j)
            answer += 1
    return answer