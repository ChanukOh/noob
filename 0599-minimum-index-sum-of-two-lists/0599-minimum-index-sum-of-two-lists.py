class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic={}
        for a,i in enumerate(list1):
            if i in list2:
                dic[i]=a
        for a,i in enumerate(list2):
            try:
                dic[i]+=a
            except:
                continue
        dic=sorted(dic.items(), key=lambda x: x[1])
        print(dic)
        a=9999999
        b=[]
        for j in dic:
            if a>=j[1]:
                a=j[1]
                b.append(j[0])
        return b