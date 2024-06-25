def solution(n, lost, reserve):
    real_lost = set(lost) - set(reserve)
    real_reserve = set(reserve) - set(lost)
    n -= len(real_lost)
    for r in sorted(real_reserve): 
        if r - 1 in real_lost:
            real_lost.remove(r - 1)
            n += 1
        elif r + 1 in real_lost:
            real_lost.remove(r + 1)
            n += 1
    return n