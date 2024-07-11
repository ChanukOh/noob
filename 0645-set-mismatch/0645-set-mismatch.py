class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        a=0

        answer=[]
        answer2=[]
        for i,j in enumerate(sorted(nums)):
            if j-a==0:
                answer.append(j)
            if j-a==2:
                answer2.append(a+1)
            a=j
        if answer2==[]:
            answer2.append(a+1)
        return answer+answer2