def solution(spell, dic):
    answer=[]
    for i in dic:
        answer.append(''.join(sorted(i)))
    b=''.join(sorted(spell))
    print(b)
    print(answer)
    return 1 if b in answer else 2