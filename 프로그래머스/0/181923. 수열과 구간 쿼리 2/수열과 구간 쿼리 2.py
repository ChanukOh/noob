def solution(arr, queries):
    answer=[]
    for a,b,c in queries:
        index=arr[a:b+1]
        for i in arr[a:b+1]:
            if i<=c:
                index.pop(index.index(i))
        if len(index)==0:
            answer.append(-1)
        else:
            answer.append(min(index))
            
    return answer