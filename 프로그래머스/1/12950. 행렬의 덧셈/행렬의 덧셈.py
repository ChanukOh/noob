def solution(arr1, arr2):
    c=[]
    for i, j in zip(arr1,arr2):
        temp=[]
        for a,b in zip(i,j):
            temp.append(a+b)
        c.append(temp)
    return c