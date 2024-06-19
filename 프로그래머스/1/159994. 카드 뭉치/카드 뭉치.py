def solution(cards1, cards2, goal):
    for i in goal:
        if i==cards1[0]:
            cards1.pop(0)
            cards1.append("!!!!!!")
        elif i==cards2[0]:
            cards2.pop(0)
            cards2.append("!!!!!!")
        else:
            return "No"
    return "Yes"