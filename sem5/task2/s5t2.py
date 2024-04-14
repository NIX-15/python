from random import randint as rand
def arrfill(k):
    alist = [rand(1,5) for i in range(k)]
    print(alist)
    return alist
def modmark(tList):
    maxi=max(tList)
    for i in range(len(tList)):
        if tList[i]==maxi:
            tList[i]=min(tList)
    return tList
a=int(input("Сколько оценок у Василия?"))
print(modmark(arrfill(a)))