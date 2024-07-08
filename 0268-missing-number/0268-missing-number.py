class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0]==1:
            return 0
        for a in nums:
            if a+1 not in nums:
                return a+1