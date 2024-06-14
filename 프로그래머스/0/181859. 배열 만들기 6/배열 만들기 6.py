def solution(arr):
    i=0
    answer = []
    while i<len(arr):
        if answer==[]:
            answer.append(arr[i])
            i+=1
        else:
            if answer[-1]==arr[i]:
                answer.pop()
                i+=1
            else:
                answer.append(arr[i])
                i+=1
    return answer if answer!=[] else [-1]