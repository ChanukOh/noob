def solution(want, number, discount):
    answer=[]
    for a,b in zip(want,number):
        for _ in range(b):
            answer.append(a)
    count=0
    i=0
    answer.sort()
    while i+len(answer)<=len(discount):
        if answer==sorted(discount[i:i+len(answer)]):
            count+=1
        i+=1
    return count