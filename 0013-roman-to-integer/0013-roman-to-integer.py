class Solution:
    def romanToInt(self, s: str) -> int:
        dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        answer=[]
        for i in s:
            answer.append(dic[i])
        count=0
        imsi=0
        for b,x in enumerate(answer):
            imsi=x
            if b+1<len(answer):
                if answer[b+1]>abs(imsi):
                    imsi=-x
            count+=imsi
        return count