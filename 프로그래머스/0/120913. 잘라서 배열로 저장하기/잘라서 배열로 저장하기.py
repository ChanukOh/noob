def solution(my_str, n):
    a=[]
    b=0
    for i in range(len(my_str)//n+(0 if len(my_str)%n==0 else 1)):
        a.append(my_str[b*n:(b+1)*n])
        b+=1
        
    return a