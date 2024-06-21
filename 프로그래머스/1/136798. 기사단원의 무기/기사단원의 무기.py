import math

def solution(number, limit, power):
    answer = [0] * (number + 1)
    for i in range(1, number + 1):
        divisor_count = 0
        sqrt_i = int(math.sqrt(i))
        for j in range(1, sqrt_i + 1):
            if i % j == 0:
                divisor_count += 1
                if j != i // j: 
                    divisor_count += 1
        if divisor_count > limit:
            answer[i] = power
        else:
            answer[i] = divisor_count
    
    return sum(answer)
