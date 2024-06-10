def solution(a, b):
    lis=[str(a),str(b)]
    ab=''.join(lis)
    ba=''.join(lis[::-1])
    if int(ab)>=int(ba):
        return int(ab)
    else:
        return int(ba)