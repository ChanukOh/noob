def solution(age):
    a=[]
    for i in str(age):
        if i=="1":
            a.append('b')
        if i=="2":
            a.append('c')
        if i=="3":
            a.append('d')
        if i=="4":
            a.append('e')
        if i=="5":
            a.append('f')
        if i=="6":
            a.append('g')
        if i=="7":
            a.append('h')
        if i=="8":
            a.append('i')
        if i=="9":
            a.append('j')
        if i=="0":
            a.append('a')
    return ''.join([str(x) for x in a])