class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s,pattern=s.split(' '),list(pattern)
        
        answer2=[]
        for k in [s,pattern]:
            dic={}
            answer1=[]
            a=1
            for i in k:
                if i in dic:
                    answer1.append(dic[i])
                else:
                    dic[i]=a
                    a+=1
                    answer1.append(dic[i])
            answer2.append(answer1)
        
        return answer2[0]==answer2[1]