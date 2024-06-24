def solution(s):
    if not s:
        return 0
    
    result_count = 0
    idx = 0
    
    while idx < len(s):
        x = s[idx]
        x_count = 0
        other_count = 0
        
        for char in s[idx:]:
            if char == x:
                x_count += 1
            else:
                other_count += 1
            
            if x_count == other_count:
                result_count += 1
                idx += x_count + other_count
                break
        else:
            result_count+=1
            break
    
    return result_count