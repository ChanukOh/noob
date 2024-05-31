def solution(answers):
    answer=[]
    a=[1,2,3,4,5]*((len(answers)//5)+2)
    b=[2,1,2,3,2,4,2,5]*((len(answers)//8)+2)
    c=[3,3,1,1,2,2,4,4,5,5]*((len(answers)//10)+2)
    acount=0
    bcount=0
    ccount=0
    for i in range(len(answers)):
        if answers[i]==a[i]:
            acount+=1
        if answers[i]==b[i]:
            bcount+=1
        if answers[i]==c[i]:
            ccount+=1

    max_count = max(acount, bcount, ccount)

    if acount == max_count:
        answer.append(1)
    if bcount == max_count:
        answer.append(2)
    if ccount == max_count:
        answer.append(3)

    return answer