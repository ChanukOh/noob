def solution(dartResult):
    scores = []
    num = ''
    i = 0
    while i < len(dartResult):
        if dartResult[i].isdigit():
            num += dartResult[i]
            if i+1 == len(dartResult) or not dartResult[i+1].isdigit():
                scores.append(int(num))
                num = ''
        elif dartResult[i] == 'S':
            scores[-1] **= 1
        elif dartResult[i] == 'D':
            scores[-1] **= 2
        elif dartResult[i] == 'T':
            scores[-1] **= 3
        elif dartResult[i] == '*':
            scores[-1] *= 2
            if len(scores) > 1:
                scores[-2] *= 2
        elif dartResult[i] == '#':
            scores[-1] *= -1
        i += 1
    
    return sum(scores)