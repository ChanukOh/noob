def solution(my_string, indices):
    my_list = list(my_string)
    for i in sorted(indices, reverse=True):
        del my_list[i]
    return ''.join(my_list)