def solution(elements):
    elem2=elements+elements
    answer=[]
    for i in range(len(elements)):
        for j in range(len(elements)):
            answer.append(sum(elem2[i:i+j+1]))
    return len(set(answer))