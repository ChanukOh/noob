def solution(price, money, count):
    double=1
    for _ in range(count):
        money-=price*double
        double+=1
    return abs(money) if money<0 else 0