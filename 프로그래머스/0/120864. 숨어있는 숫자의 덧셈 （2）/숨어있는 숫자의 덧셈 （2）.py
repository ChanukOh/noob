def solution(my_string):
    table = str.maketrans('abcdefghijklmnopqrstuvwxyz', '!!!!!!!!!!!!!!!!!!!!!!!!!!')
    my_string=my_string.lower()
    my_string=my_string.translate(table)
    return sum(int(i) for i in my_string.split('!') if i.isdigit())