def solution(myString, pat):
    count=[]
    for b in range(len(myString)-len(pat)+1):
        if pat in myString[b:b+len(pat)]:
            count.append(b)
    return len(count)