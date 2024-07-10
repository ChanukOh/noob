class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic={}
        for i in s:
            dic[i]=dic.get(i,0)+1
        for i,j in enumerate(s):
            if dic[j]==1:
                return i
        return -1