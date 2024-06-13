def solution(arr):
    a=1
    while a<len(arr):
        a*=2
    for i in range(a):
        try:
            if arr[i] is None:
                arr.append(0)
        except:
            arr.append(0)
    return arr