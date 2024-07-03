def solution(s):
    return ' '.join(map(str,[min(map(int,s.split())),max(map(int,s.split()))]))