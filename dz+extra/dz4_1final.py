var1 = '5 4' # количество элементов первого и второго множества
var2 = '1 3 5 7 9' # элементы первого множества через пробел
var3 = '2 3 4 5' # элементы второго множества через пробел
set2=set(var2.split())
set3=set(var3.split())
result=sorted(set2.intersection(set3))
print(" ".join(result))