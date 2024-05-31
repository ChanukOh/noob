def solution(id_list, report, k):
    reporter={}
    reported={}
    stop=[]
    stopper={}
    for i in id_list:
        stopper[i]=0
        reporter[i]=[]
        reported[i]=0
        
    for i in report:
        i = i.split()
        if i[1] not in reporter[i[0]]:
            reporter[i[0]].append(i[1])
            reported[i[1]]=reported[i[1]]+1
    for i in reported.keys():
        if reported[i]>=k:
            stop.append(i)

    
        
    for key,value in reporter.items():
        found_counts=0
        for elem in stop:
            found_counts += value.count(elem)
        stopper[key]=found_counts
        
    return [stopper[i] for i in id_list]