def solution(id_pw, db):
    dic={}
    for id,pw in db:
        dic[id]=pw
    try:
        if dic[id_pw[0]]==id_pw[1]:
            return "login"
        else:
            return "wrong pw"
    except:
        return "fail"