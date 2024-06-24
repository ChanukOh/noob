def solution(babbling):
    answer = 0
    for i in babbling:
        if 'aya' in i:
            i=i.replace('aya','1')
        if 'ye' in i:
            i=i.replace('ye','2')
        if 'woo' in i:
            i=i.replace('woo','3')
        if 'ma' in i:
            i=i.replace('ma','4')
        a='0'
        death=0
        for j in i:
            if j==a:
                death=1
                pass
            else:
                a=j
        if death==0:
            i=i.replace('1','')
            i=i.replace('2','')
            i=i.replace('3','')
            i=i.replace('4','')
            if i=='':
                answer+=1
    return answer