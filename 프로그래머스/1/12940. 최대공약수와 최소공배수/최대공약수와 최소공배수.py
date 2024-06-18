def solution(n, m):
    n_yak=[]
    m_yak=[]
    for i in range(1,n+1):
        if n%i==0:
            n_yak.append(i)
    for i in range(1,m+1):
        if m%i==0:
            m_yak.append(i)
    n_yak.sort(reverse=True)
    for i in n_yak:
        if i in m_yak:
            return [i,(n*m)/i]
    return n_yak