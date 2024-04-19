print(old_list:=[i+1 for i in range(20)])
print((lambda old_: [(i, i**2) for i in old_ if i%2==0])(old_list))