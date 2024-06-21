from itertools import combinations
import math

def is_prime(n):
    if n <= 1:
        return 0
    if n == 2:
        return 1
    if n % 2 == 0:
        return 0
    sqrt_n = int(math.sqrt(n))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return 0
    return 1

def solution(nums):
    a=combinations(nums,3)
    b=0
    for i in a:
        b+=is_prime(sum(i) )

    return b