class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        z=[]
        for x in digits:
            z.append(str(x))
        y=int(''.join(z))+1
        z=[]
        for x in str(y):
            z.append(int(x))
        return z