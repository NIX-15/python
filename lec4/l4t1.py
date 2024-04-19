import itertools
# print(old_list:=[i+1 for i in range(20)])
# print((lambda old_: [(i, i**2) for i in old_ if i%2==0])(old_list))

print(old_list:=input("Input Data: "))
new_list=list(old_list)
print(new_list)
new_list=list(filter(lambda item:not item.isalpha(),new_list))
new_list=map(int,new_list)
new_list=list(map(lambda x:(x,x**3,round(x**-3,4)) if x%2!=0 else x, new_list))
print(new_list)