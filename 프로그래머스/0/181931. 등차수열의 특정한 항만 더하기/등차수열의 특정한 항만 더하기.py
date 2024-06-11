def solution(a, d, included):
    answer = 0
    b=list(range(a,a+d*len(included)))[0::d]
    for i,c in enumerate(b):
        if included[i]==True:
            answer+=c
    return answer