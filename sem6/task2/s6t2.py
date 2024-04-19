def bothless(al):
    result=0
    for i in range(1,len(al)-1):
        if al[i+1]<al[i]>al[i-1]:
            result+=1
    return result
dlin=int(input("Введите длину списка: "))
alist=[int(input()) for _ in range(dlin)]
print(alist)
print(bothless(alist))