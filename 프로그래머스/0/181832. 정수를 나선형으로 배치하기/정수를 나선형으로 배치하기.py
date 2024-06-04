def solution(n):
    # n x n 배열 초기화
    array = [[0] * n for _ in range(n)]
    
    num = 1  
    top, bottom, left, right = 0, n-1, 0, n-1 
    
    while num <= n*n:
        for i in range(left, right+1):
            array[top][i] = num
            num += 1
        top += 1
        
        for i in range(top, bottom+1):
            array[i][right] = num
            num += 1
        right -= 1
        
        for i in range(right, left-1, -1):
            array[bottom][i] = num
            num += 1
        bottom -= 1
        
        for i in range(bottom, top-1, -1):
            array[i][left] = num
            num += 1
        left += 1
    
    return array