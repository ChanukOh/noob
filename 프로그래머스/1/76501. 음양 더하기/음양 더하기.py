def solution(absolutes, signs):
    z=0
    for i,a in enumerate(absolutes):
        if signs[i]==True:
            z+=a
        else:
            z-=a
    return z