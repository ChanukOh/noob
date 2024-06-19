def solution(leng, arr1, arr2):
    def decimal_to_binary(n):
        binary = bin(n)[2:]
        return '0' * (leng - len(binary)) + binary if len(binary) < leng else binary
    answer = [list(decimal_to_binary(i)) for i in arr1]
    answer2= [list(decimal_to_binary(i)) for i in arr2]
    mp=[]
    for i in range(leng):
        mpp=[]
        for j in range(leng):
            if answer[i][j]=="1" or answer2[i][j]=="1":
                mpp.append('#')
            else:
                mpp.append(" ")
        mp.append(''.join(mpp))
    return mp