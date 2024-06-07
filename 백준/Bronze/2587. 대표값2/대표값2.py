import statistics
a = []
for i in range(5):
    a.append(int(input()))
a.sort()
print(statistics.mean(a))
print(a[len(a)//2])