def solution(picture, k):
    answer = []
    for i in picture:
        b=[]
        for j in i:
            b.append(j*k)
        for _ in range(k):
            answer.append(''.join(b))
    return answer