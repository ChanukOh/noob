
N = int(input())

a = []
b=0
a=set(a)
for i in range(N):
    s = input()
    a.add(s)
    if len(s) > b:
        b = len(s)

a2 = sorted(a, key=lambda x:(len(x),x*b))
for i in a2:    
    print(i)