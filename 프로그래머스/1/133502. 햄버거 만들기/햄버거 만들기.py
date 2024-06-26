def solution(ingredient):
    b = 0
    stack = ingredient[:]
    n = len(stack)
    
    i = 0
    while i < n - 3:
        if stack[i:i+4] == [1, 2, 3, 1]:
            del stack[i:i+4]
            b += 1
            n -= 4
            i = max(0, i - 4)
        else:
            i += 1
    
    return b

    return b
