def solution(s):
    answer = []
    seen = {}
    for i, char in enumerate(s):
        if char in seen:
            answer.append(i - seen[char])
        else:
            answer.append(-1)
        seen[char] = i
    return answer