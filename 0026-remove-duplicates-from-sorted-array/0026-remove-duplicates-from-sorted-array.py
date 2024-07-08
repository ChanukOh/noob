class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        answer=nums[:]
        nums.clear()
        for i in answer:
            if i not in nums:
                nums.append(i)
        return len(nums)

        