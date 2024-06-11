def solution(arr, n):
    answer=[]
    if len(arr)%2==1:
        for i,a in enumerate(arr):
            if i%2==0:
                answer.append(a+n)
            else:
                answer.append(a)
    if len(arr)%2==0:
        for i,a in enumerate(arr):
            if i%2==1:
                answer.append(a+n)
            else:
                answer.append(a)
    return answer