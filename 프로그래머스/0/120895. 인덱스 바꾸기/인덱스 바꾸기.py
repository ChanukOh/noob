def solution(my_string, num1, num2):
    a=my_string[num1]
    b=my_string[num2]
    my_string=list(my_string)
    my_string[num1]=b
    my_string[num2]=a
    return ''.join(i for i in my_string)