def solution(food):
    answer=[]
    for i,a in enumerate(food):
        if a//2!=0:
            for j in range(a//2):
                answer.append(i)
    answer2=answer[::-1]
    answer.append(0)
    answer=answer+answer2
    return ''.join(map(str,answer))