aboba=input("Пишите слово: ")
uniqsym=set(aboba)
uniqlist=list(uniqsym)
del uniqsym
mydict=dict()
result=''
for i in range(len(uniqlist)):
    mydict[uniqlist[i]]=0
for char in range(len(aboba)):
    if mydict[aboba[char]]!=0:
        result+=aboba[char]+"_"+str(mydict[aboba[char]])
        mydict[aboba[char]]+=1
    else:
        result+=aboba[char]
        mydict[aboba[char]]+=1
print(mydict)
print(result)