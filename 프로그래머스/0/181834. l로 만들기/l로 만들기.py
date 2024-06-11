a='abcdefghijk'
def solution(myString):
    answer = []
    for i in myString:
        if i in a:
            answer.append('l')
        else:
            answer.append(i)
    return ''.join(answer)