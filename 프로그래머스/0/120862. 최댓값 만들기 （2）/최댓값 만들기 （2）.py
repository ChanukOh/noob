def solution(numbers):
    numbers.sort()
    if numbers[-1]*numbers[-2]<=numbers[1]*numbers[0]:
        return numbers[0]*numbers[1]
    else:
        return numbers[-1]*numbers[-2]