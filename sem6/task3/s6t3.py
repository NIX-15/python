def pairs(alist):
    if len(alist)>1:
        for i in range(len(alist)):
            for j in range(i+1,len(alist)):
                if alist[j]==alist[i]:
                    alist.pop(j)
                    alist.pop(i)
                    return pairs(alist)
    return alist
size=int(input("Размер списка: "))
lista=[int(input("Вводите числа:")) for _ in range(size)]
print(f'Кол-во пар одинаковых чисел:{(len(lista)-len(pairs(lista)))//2}')