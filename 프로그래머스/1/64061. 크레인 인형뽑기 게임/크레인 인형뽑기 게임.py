def solution(board, moves):
    b=0
    prize=[]
    for i in moves:
        a=0
        while board[a][i-1]==0:
            a+=1
            if a==len(board)-1:
                break
        if board[a][i-1]==0:
            continue
        else:
            c=board[a][i-1]
            board[a][i-1]=0
        if len(prize)>0:
            if prize[-1]==c:
                prize.pop(-1)
                b+=2
                continue
            else:   
                prize.append(c)
        else:
            prize.append(c)
    return b