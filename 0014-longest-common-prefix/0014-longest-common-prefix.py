class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer=[]
        strs.sort(key=lambda x:len(x))
        globalcheck=0
        for i,x in enumerate(strs[0]):
            for j in range(1,len(strs)):
                if strs[j][i]!=strs[0][i]:
                    globalcheck=1
                    return ''.join(answer)
            if globalcheck==0:
                answer.append(x)
        return ''.join(answer)