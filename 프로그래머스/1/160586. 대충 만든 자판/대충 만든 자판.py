def solution(keymap, targets):
    answer = {}
    alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for b in alpha:
        answer[b]=10000
    for i in keymap:
        for j,a in enumerate(i):
            if answer[a]>j+1:
                answer[a]=j+1
    count=[]
    for c in targets:
        xy=0
        for d in c:
            xy+=answer[d]
        if xy>=10000:
            count.append(-1)
        else:
            count.append(xy)
    return count