def solution(order):
    americano=0
    cafelatte=0
    for i in order:
        if "cafelatte" in i:
            cafelatte+=5000
        else:
            americano+=4500
    return americano+cafelatte