
def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        row = i // n  # 현재 인덱스의 행
        col = i % n   # 현재 인덱스의 열
        value = max(row, col) + 1
        answer.append(value)
    return answer