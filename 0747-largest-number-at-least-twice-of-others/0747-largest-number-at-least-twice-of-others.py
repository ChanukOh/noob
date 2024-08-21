class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        nums2=[]
        n=max(nums)
        for i in nums:
            if i!=n:
                nums2.append(i*2)
        m=max(nums2)
        
        return nums.index(n) if n>=m else -1