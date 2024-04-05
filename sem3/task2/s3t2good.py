import random
sizee,k=5,1
list1=[random.randint(-10,10) for _ in range(sizee)]
print(list1)
list2=list1.copy()
for i in range(sizee):
    ni=i-k
    while(abs(ni)>sizee-1):
        ni=ni+sizee
    list2[i]=list1[ni]
print(list2)
del list1