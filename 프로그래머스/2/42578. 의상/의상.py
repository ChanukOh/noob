def solution(clothes):
    answer = {}
    total_combinations = 1
    
    for cloth_type in clothes:
        answer[cloth_type[1]] = answer.get(cloth_type[1], 0) + 1
        
    for count in answer.values():
        total_combinations *= (count + 1) 
        
    total_combinations -= 1
    
    return total_combinations