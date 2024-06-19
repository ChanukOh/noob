def solution(name, yearning, photo):
    humans={}
    for i in range(len(name)):
        humans[name[i]]=yearning[i]
    total_score=[]
    for x in photo:
        score=[]
        for y in x:
            score.append(humans.get(y,0))
        total_score.append(sum(score))
    return total_score