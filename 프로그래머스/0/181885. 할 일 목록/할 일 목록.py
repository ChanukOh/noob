def solution(todo_list, finished):
    answer=[]
    for i,a in enumerate(todo_list):
        if finished[i]==False:
            answer.append(a)
    return answer