def solution(num_list):
    odd=[]
    even=[]
    for i,a in enumerate(num_list):
        if i%2==0:
            even.append(a)
        else:
            odd.append(a)
    odd=sum(odd)
    even=sum(even)
    return odd if odd>=even else even