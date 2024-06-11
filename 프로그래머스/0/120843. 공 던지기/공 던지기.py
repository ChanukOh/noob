def solution(numbers, k):
    a=numbers*2*(k//(len(numbers))+1)
    b=a[::2]
    return b[k-1]