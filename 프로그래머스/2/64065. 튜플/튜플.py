def solution(s):
    sets = s[2:-2].split("},{")
    sets.sort(key=lambda x: len(x))
    
    answer = []
    for subset in sets:
        numbers = list(map(int, subset.split(',')))
        for num in numbers:
            if num not in answer:
                answer.append(num)
    
    return answer