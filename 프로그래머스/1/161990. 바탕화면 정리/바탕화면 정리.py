def solution(wallpaper):
    y2=[]
    x2=[]
    for i,a in enumerate(wallpaper):
        for j,b in enumerate(a):
            if b=='#':
                x2.append(j)
                y2.append(i)
    return min(y2),min(x2),max(y2)+1,max(x2)+1