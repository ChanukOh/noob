def solution(s, skip, index):
    i=0
    dic={}
    answer=[]
    answer2=[]
    alpha='abcdefghijklmnopqrstuvwxyz'
    for a in alpha:
        if a in skip:
            continue
        dic[a] = i
        dic[i] = a
        i += 1

    for j in s:
        answer.append(dic[j]+index)
    for x in answer:
        x=x%(26-len(skip))
        answer2.append(dic[x]) 
    return ''.join(answer2)