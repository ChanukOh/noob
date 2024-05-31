def solution(keyinput, board):
    x=0
    y=0
    for i in keyinput:
        if i=="up":
            if y<board[1]//2:
                y+=1
        if i=="down":
            if y>-(board[1]//2):
                y-=1
        if i=="left":
            if x>-(board[0]//2):
                x-=1
        if i=="right":
            if x<board[0]//2:
                x+=1
    return [x,y]