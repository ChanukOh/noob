def solution(s):
    def is_valid(s):
        stack = []
        brackets = {'(': ')', '[': ']', '{': '}'}
        for char in s:
            if char in brackets:
                stack.append(char)
            elif char in brackets.values():
                if not stack or brackets[stack.pop()] != char:
                    return False
        return len(stack) == 0
    
    n = len(s)
    answer = 0
    
    for i in range(n):
        rotated_s = s[i:] + s[:i]
        if is_valid(rotated_s):
            answer += 1
    
    return answer