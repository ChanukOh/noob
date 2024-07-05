def solution(n, words):
    answer = [0,0]
    dic={}
    for i,a in enumerate(words):
        dic[a]=dic.get(a,0)+1
        if i==0:
            continue
        else:
            if words[i-1][-1]!=words[i][0]:
                answer=[(i%n)+1,(i//n)+1]
                return answer
            elif dic[a]>1:
                answer=[(i%n)+1,(i//n)+1]
                return answer
    return answer