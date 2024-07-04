from itertools import permutations
import math
def solution(numbers):
    perm_list = []
    
    for r in range(len(numbers)):
        perms = permutations(numbers, r+1)
        for perm in perms:
            perm_list.append(int(''.join(perm)))
    def is_prime(num):
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        sqrt_num = int(math.sqrt(num)) + 1
        for divisor in range(3, sqrt_num, 2):
            if num % divisor == 0:
                return False

        return True
    answer=[]
    for perm in set(perm_list):
        if is_prime(perm)==True:
            answer.append(perm)
    
    return len(answer)