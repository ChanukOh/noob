def solution(M, N):
    cut=0
    stack=[M*N]
    while stack:
        a=stack.pop()
        if a!=1:
            if a%2==0:
                stack.append(a/2)
                stack.append(a/2)
                cut+=1
            else:
                stack.append(a-1)
                stack.append(1)
                cut+=1
    return cut