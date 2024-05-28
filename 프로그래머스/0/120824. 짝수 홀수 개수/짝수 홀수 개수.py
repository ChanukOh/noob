def solution(num_list):
    gen=[]
    baku=[]
    for i in num_list:
        if i%2==1:
            baku.append(i)
        else:
            gen.append(i)
    return [len(gen),len(baku)]