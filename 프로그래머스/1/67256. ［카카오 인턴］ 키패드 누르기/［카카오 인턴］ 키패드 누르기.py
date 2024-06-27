def distance_between_points(x1, y1, x2, y2):
    distance = abs(x2 - x1) + abs(y2 - y1)
    return distance

def solution(numbers, hand):
    answer = []
    if hand == 'left':
        hand = "L"
    else:
        hand = "R"
        
    dic = {
        '1': [0, 0], '2': [0, 1], '3': [0, 2],
        '4': [1, 0], '5': [1, 1], '6': [1, 2],
        '7': [2, 0], '8': [2, 1], '9': [2, 2],
        '*': [3, 0], '0': [3, 1], '#': [3, 2]
    }

    left = dic['*'] 
    right = dic['#']  
    
    for num in numbers:
        num_str = str(num)
        if num_str in ['1', '4', '7']:  
            answer.append('L')
            left = dic[num_str]
        elif num_str in ['3', '6', '9']: 
            answer.append('R')
            right = dic[num_str]
        else:  
            dist_left = distance_between_points(left[0], left[1], dic[num_str][0], dic[num_str][1])
            dist_right = distance_between_points(right[0], right[1], dic[num_str][0], dic[num_str][1])
            
            if dist_left < dist_right: 
                answer.append('L')
                left = dic[num_str]
            elif dist_left > dist_right:  
                answer.append('R')
                right = dic[num_str]
            else:  
                answer.append(hand)
                if hand == "L":
                    left = dic[num_str]
                else:
                    right = dic[num_str]

    return ''.join(answer)
