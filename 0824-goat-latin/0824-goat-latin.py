class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        answer=[]
        moum=['a','e','i','o','u','A','E','I','O','U']
        a=sentence.split(' ')
        for x,i in enumerate(a):
            imsi=[]
            if i[0] not in moum:
                imsi.append(i[1:])
                imsi.append(i[0])
                imsi.append('ma')
            else:
                imsi.append(i)
                imsi.append('ma')
            for j in range(x+1):
                imsi.append('a')
            answer.append(''.join(imsi))
        return ' '.join(answer)