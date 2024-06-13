def solution(arr, flag):
    x=[]
    for i,a in enumerate(flag):
        if a==True:
            for time in range(2*arr[i]):
                x.append(arr[i])
        else:
            for time in range(arr[i]):
                x.pop()
        
    return x