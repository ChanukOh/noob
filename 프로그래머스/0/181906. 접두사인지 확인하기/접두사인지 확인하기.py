def solution(my_string, is_prefix):
    a=[]
    for i,e in enumerate(my_string):
        a.append(my_string[:i])
        
    if is_prefix in a:
        return 1
    return 0