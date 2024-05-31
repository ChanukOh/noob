def solution(nums):
    answer = list(set(nums))
    
    return len(nums)/2 if len(answer)>=len(nums)/2 else len(answer)