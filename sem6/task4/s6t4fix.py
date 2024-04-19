def sumdel(num):
    res=1
    for i in range(2, num//2+1):
        if num%i==0:
            res+=i
    return res
def fill_list(alist,k):
    for i in range(k+1):
        alist.append([i,sumdel(i)])
    return alist
def friends(full_list):
    result=list()
    for i in range(len(full_list)-1):
        for j in range(i+1,len(full_list)):
            if full_list[j][1]==full_list[i][0] and full_list[j][0]==full_list[i][1]:
                result.append([i,j])
    return result
num_list=[]
limit=10000
fill_list(num_list,limit)
print("Result: ",friends(num_list))