N = int(input())

a = []

for i in range(N):
    a.append(list(map(int, input().split())))

a2 = sorted(a, key=lambda x:(x[0], x[1]))
for i in a2:    
    print(i[0],i[1])