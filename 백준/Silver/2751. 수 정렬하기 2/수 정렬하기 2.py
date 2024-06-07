import sys

input_ = sys.stdin.readline

N = int(input_())

a = []

for i in range(N):
    a.append(int(input_()))
a.sort()
for i in a:
    print(i)