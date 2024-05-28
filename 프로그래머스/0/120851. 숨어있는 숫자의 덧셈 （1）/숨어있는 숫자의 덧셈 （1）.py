def solution(my_string):
    num=[]
    for i in my_string:
        if i.isdigit():
            if int(i)==1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 0:
                num.append(int(i))
    return sum(num)