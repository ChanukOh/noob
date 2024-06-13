def solution(myString, pat):
    a=myString[::-1].find(pat[::-1])
    b=a
    
    return myString[:len(myString)-b]
