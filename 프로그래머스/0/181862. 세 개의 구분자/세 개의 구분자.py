import re
def solution(myStr):
    a=re.split('[abc]', myStr)
    b=[]
    for i in a:
        if i!="":
            b.append(i)
    return b if b!=[] else ["EMPTY"]