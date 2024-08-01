answer=int(input())
count=int(input())
a=0
for i in range(count):
    item,num=input().split()
    a+=int(item)*int(num)
if a==answer:
    print("Yes")
else:
    print("No")