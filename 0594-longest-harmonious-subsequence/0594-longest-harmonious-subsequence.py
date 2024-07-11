from typing import List
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        max_length = 0
        for key in dic:
            if key + 1 in dic:
                max_length = max(max_length, dic[key] + dic[key + 1])
        return max_length