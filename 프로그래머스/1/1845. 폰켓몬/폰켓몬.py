def solution(nums):
    answer={}
    for i in nums:
        answer[i]=0
    return min([len(nums)/2,len(answer)])