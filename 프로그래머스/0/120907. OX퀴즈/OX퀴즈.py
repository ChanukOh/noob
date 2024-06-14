def solution(quiz):
    answer = []
    b=[]
    for i in quiz:
        for j in i:
            if j==' ':
                answer.append(''.join(b))
                b=[]
            else:
                b.append(j)
        answer.append(''.join(b))
        b=[]
    ox=[]
    for i in range(len(quiz)):
        x=int(answer[i*5])
        y=int(answer[i*5+2])
        z=int(answer[i*5+4])
        if answer[i*5+1]=="-":
            ox.append("X") if x-y!=z else ox.append("O")
        if answer[i*5+1]=="+":
            ox.append("X") if x+y!=z else ox.append("O")
        
    return ox