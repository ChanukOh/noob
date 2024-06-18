
def solution(s):
    zxc = s.split(' ') 
    answer = []
    
    for y in zxc:
        s_list = list(y)
        for i, a in enumerate(s_list):
            if i % 2 == 0:
                s_list[i] = a.upper()
            else:
                s_list[i] = a.lower() 
        answer.append(''.join(s_list))
        
    return ' '.join(answer)