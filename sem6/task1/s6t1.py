def lists_dif(li_a,li_b):
    result=list()
    return [i for i in li_a if i not in li_b] or "Nothing!"
list_a=list_b=list()
n=int(input("Размер списка 1: "))
m=int(input("Размер списка 2: "))
list_a=[int(input("list1: ")) for i in range(n)]
list_b=[int(input("list2: ")) for i in range(m)]
print(list_a,list_b)
print(lists_dif(list_a,list_b))