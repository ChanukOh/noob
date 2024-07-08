class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        a=1
        trashbin={}
        x=[]
        y=[]
        for i in s:
            if i not in trashbin:
                trashbin[i]=a
                a+=1
            x.append(trashbin[i])
        a=1
        trashbin={}    
        for i in t:
            if i not in trashbin:
                trashbin[i]=a
                a+=1
            y.append(trashbin[i])
        
        return x==y