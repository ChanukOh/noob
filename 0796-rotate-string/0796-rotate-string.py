class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        a=0
        s=s
        while a<len(s):
            if s==goal:
                return True
            else:
                s=s[-len(s)+1:]+s[:-len(s)+1]
                a+=1
                print(s)
        return False