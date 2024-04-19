def rever(st):
    if len(st)<dlin:
        ch=input()
        if(len(ch))>1:
            print("only 1 character")
            return rever(st)
        st=ch+st
        return rever(st)
    return st

dlin=3
strok=''
ch=''

print(rever(strok))