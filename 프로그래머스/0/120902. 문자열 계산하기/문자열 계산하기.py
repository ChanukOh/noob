def solution(my_string):
    answer = my_string.replace("-","+").replace(" ","").split("+")
    b=0
    c=int(answer[0])
    for i in my_string:
        if i=="+":
            b+=1
            c=c+int(answer[b])
        if i=="-":
            b+=1
            c=c-int(answer[b])
    return c