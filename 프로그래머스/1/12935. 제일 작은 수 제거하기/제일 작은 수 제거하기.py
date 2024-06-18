def solution(arr):
    a=sorted(arr,reverse=True)
    b=arr.index(a[-1])
    arr.pop(b)
    return arr if len(arr)!=0 else [-1]