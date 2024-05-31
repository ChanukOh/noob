def solution(my_string):
    dic={}
    answer=[]
    for i in my_string:
        if i in dic:
            pass
        else:
            dic[i]=1
            answer.append(i)
    return "".join(answer)