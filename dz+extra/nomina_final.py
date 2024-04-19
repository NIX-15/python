def baks(summ,n,i,res):
    if summ==0:
        return res
    if summ<n[i]:
        return baks(summ,n,i-1,res)
    if str(n[i])+'$' not in res:
        res[str(n[i])+'$']=1
        summ-=n[i]
        return baks(summ,n,i,res)
    res[str(n[i])+'$']+=1
    summ-=n[i]
    return baks(summ,n,i,res)
nom=(1,2,5,10,20,50,100,)
summa=int(input("Введите сумму $: "))
result=dict()
print(baks(summa,nom,-1,result))