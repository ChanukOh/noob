def solution(q, r, code):
    answer = []
    for i,a in enumerate(code):
        if i%q==r:
            answer.append(a)
    return ''.join(answer)