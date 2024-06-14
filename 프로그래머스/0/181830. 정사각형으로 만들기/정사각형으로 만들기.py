def solution(arr):
    x = len(arr[0])
    y = len(arr)
    max_len = max(x, y)
    for i in range(max_len - y):
        arr.append([0] * x)
    for row in arr:
        for i in range(max_len - x):
            row.append(0)
    return arr