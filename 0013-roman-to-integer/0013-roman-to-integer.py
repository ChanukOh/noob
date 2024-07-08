class Solution:
    def romanToInt(self, s: str) -> int:
        dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        count=0
        imsi=0
        for b,y in enumerate(s):
            x=dic[y]
            imsi=x
            if b+1<len(s):
                if dic[s[b+1]]>abs(imsi):
                    imsi=-x
            count+=imsi
        return count