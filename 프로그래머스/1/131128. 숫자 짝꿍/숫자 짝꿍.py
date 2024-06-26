from collections import Counter

def solution(X, Y):
    count_X = Counter(str(X))
    count_Y = Counter(str(Y))
    common_digits = set(count_X.keys()) & set(count_Y.keys())
    max_pairable_digits = []
    for digit in common_digits:
        max_pairs = min(count_X[digit], count_Y[digit])
        max_pairable_digits.extend([digit] * max_pairs)
    max_pairable_digits.sort(reverse=True)
    if not max_pairable_digits:
        return "-1"
    if all(digit == '0' for digit in max_pairable_digits):
        return "0"
    return ''.join(max_pairable_digits)
