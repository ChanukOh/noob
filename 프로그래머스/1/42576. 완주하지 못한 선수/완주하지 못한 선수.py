def solution(participant, completion):
    participant_count={}
    for p in participant:
        participant_count[p]=participant_count.get(p,0)+1
    for c in completion:
        participant_count[c]-=1
    for p,count in participant_count.items():
        if count>0:
            return p
    