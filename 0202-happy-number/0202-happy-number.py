class Solution:
    def isHappy(self, n: int) -> bool:
        a=[]
        b=0
        while True:
            for i in list(str(n)):
                b+=(int(i)**2)
            if b==1:
                return True
            if b in a:
                return False
            else:
                a.append(b)
                n=b
                b=0