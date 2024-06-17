def solution(babbling):
    answer = 0
    for i in babbling:
        if 'aya' in i:
            i=i.replace('aya','1')
        if 'ye' in i:
            i=i.replace('ye','1')
        if 'woo' in i:
            i=i.replace('woo','1')
        if 'ma' in i:
            i=i.replace('ma','1')
        i=i.replace('1','')
        if i=='':
            answer+=1
    return answer