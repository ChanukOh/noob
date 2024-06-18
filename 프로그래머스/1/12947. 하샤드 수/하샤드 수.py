def solution(x):
    a=[int(i) for i in str(x)]
    if x%sum(a)==0:
        return True
    return False