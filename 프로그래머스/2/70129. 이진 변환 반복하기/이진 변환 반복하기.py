def solution(s):
    count_transform = 0
    count_removed_zeros = 0
    while s != "1":
        count_removed_zeros += s.count('0')
        c = s.count('1')
        s = bin(c)[2:]
        count_transform += 1
    return [count_transform, count_removed_zeros]
