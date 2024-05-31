def solution(nums):
    answer = list(set(nums))
    
    return min([len(nums)/2,len(answer)])