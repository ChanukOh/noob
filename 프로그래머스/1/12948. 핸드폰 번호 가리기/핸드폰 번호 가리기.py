def solution(phone_number):
    answer = []
    c=0
    for i in phone_number[::-1]:
        if c>3:
            answer.append('*')
        else:
            answer.append(i)
            c+=1
    answer=''.join(answer)
    return answer[::-1]