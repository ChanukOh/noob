def solution(n):
    one_count = bin(n).count('1')
    next_number = n + 1
    while True:
        if bin(next_number).count('1') == one_count:
            return next_number
        next_number += 1