class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s,pattern=s.split(' '),list(pattern)
        dic={}
        answer1=[]
        answer2=[]
        a=1
        for i in s:
            if i in dic:
                answer1.append(dic[i])
            else:
                dic[i]=a
                a+=1
                answer1.append(dic[i])
        a=1
        dic={}
        for i in pattern:
            if i in dic:
                answer2.append(dic[i])
            else:
                dic[i]=a
                a+=1
                answer2.append(dic[i])
        return answer1==answer2