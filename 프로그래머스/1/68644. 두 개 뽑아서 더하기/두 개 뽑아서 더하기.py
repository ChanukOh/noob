from itertools import combinations
def solution(numbers):
    a=[]
    combs = combinations(numbers, 2)
    for comb in combs:
        a.append(sum(comb))
    return sorted(list(set(a)))
        