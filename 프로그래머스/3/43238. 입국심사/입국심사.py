def solution(n, times):
    left = 1 
    right = max(times) * n 
    answer = right 
    while left <= right:
        mid = (left + right) // 2
        total_people = sum(mid // t for t in times)
        print(total_people,mid,n)
        if total_people < n:
            left = mid + 1
        else:
            right = mid - 1
            print(total_people,mid)
            answer = mid  
    return answer