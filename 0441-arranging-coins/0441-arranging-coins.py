class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n==1:
            return 1
        a=1
        b=0
        while n>0:
            n-=a
            a+=1
            b+=1
        return b-1