class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        answer=nums[:]
        nums.clear()
        for i in range(len(answer)):
            if answer[i]!=val:
                nums.append(answer[i])
        return len(nums)