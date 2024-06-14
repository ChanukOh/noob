def solution(arr):
    arr2=arr[::-1]
    try:
        a=arr.index(2)
        b=arr2.index(2)
    except:
        return [-1]
    return arr[a:len(arr)-b]