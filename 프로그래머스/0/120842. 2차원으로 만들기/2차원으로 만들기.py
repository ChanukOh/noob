def solution(num_list, n):
    return [[num_list[i+(b*n)] for i in range(n)]for b in range(len(num_list)//n)]