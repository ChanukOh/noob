def solution(lottos, win_nums):
    win_nums.sort()
    lottos.sort()
    b=0
    c=0
    for i,a in enumerate(lottos):
        if a==0:
            c+=1
        else:
            if a in win_nums:
                b+=1
    print(win_nums)
    print(lottos)
    dic={6:1,
        5:2,
        4:3,
        3:4,
        2:5,
        1:6,
        0:6}
    return [dic[b+c],dic[b]]