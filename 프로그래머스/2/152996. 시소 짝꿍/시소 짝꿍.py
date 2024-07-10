def solution(weights):
    answer = 0
    count_map = {}
    for weight in weights:
        if weight in count_map:
            count_map[weight] += 1
        else:
            count_map[weight] = 1
    unique_weights = sorted(count_map.keys())  
    n = len(unique_weights)
    for i in range(n):
        a = unique_weights[i]
        for j in range(i, n):
            b = unique_weights[j]
            if (a == b or 
                a * 3 == 2 * b or a * 2 == b or  a == b * 2 or
                a * 3 == 4 * b or a * 4 == 3 * b or 
                a * 2 == 3 * b):
                
                if a == b:
                    answer += count_map[a] * (count_map[a] - 1) // 2
                else:
                    answer += count_map[a] * count_map[b]
    return answer