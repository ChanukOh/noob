def solution(survey, choices):
    # 성격 유형 점수를 저장할 딕셔너리
    dic = {
        "R": 0,
        "T": 0,
        "C": 0,
        "F": 0,
        "J": 0,
        "M": 0,
        "A": 0,
        "N": 0
    }

    # 각 질문에 대해 점수 계산
    for i in range(len(survey)):
        a, b = survey[i][0], survey[i][1]
        choice = choices[i]
        
        if choice > 4:
            dic[b] += choice - 4
        elif choice < 4:
            dic[a] += 4 - choice
    result = ""
    result += 'R' if dic['R'] >= dic['T'] else 'T'
    result += 'C' if dic['C'] >= dic['F'] else 'F'
    result += 'J' if dic['J'] >= dic['M'] else 'M'
    result += 'A' if dic['A'] >= dic['N'] else 'N'
    return result