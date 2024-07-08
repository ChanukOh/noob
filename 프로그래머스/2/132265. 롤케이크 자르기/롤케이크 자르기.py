def solution(topping):
    answer = 0
    left_count = {}
    right_count = {}
    for topping_type in topping:
        right_count[topping_type] = right_count.get(topping_type, 0) + 1
    for a in range(len(topping)):
        topping_type = topping[a]
        left_count[topping_type] = left_count.get(topping_type, 0) + 1
        right_count[topping_type] -= 1
        if right_count[topping_type] == 0:
            del right_count[topping_type]
        if len(left_count) == len(right_count):
            answer += 1
    
    return answer