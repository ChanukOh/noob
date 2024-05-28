def solution(array):
    max_value = max(array)
    max_indices = [i for i, v in enumerate(array) if v == max_value]
    return [max_value, max_indices[0]]