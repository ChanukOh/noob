dic={}
for i in str(input()):
    dic[i.upper()]=dic.get(i.upper(),0)+1
sorted_dic = dict(sorted(dic.items(), key=lambda item: item[1]))
if len(list(sorted_dic.keys()))!=1:
    if dic[list(sorted_dic.keys())[-1]]==dic[list(sorted_dic.keys())[-2]]:
        print('?')
    else:
        print(list(sorted_dic.keys())[-1])
else:
        print(list(sorted_dic.keys())[-1])