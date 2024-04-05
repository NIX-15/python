from string import punctuation
stringi = '''
	a-1
	b-2
	c-3
	d-4
	e-5
'''
# Разбейте эту строку в словарь следующим образом:

# {
# 	'a': 1
# 	'b': 2
# 	'c': 3
# 	'd': 4
# 	'e': 5
# }
print(stringi)
dickt = dict()
# for i in punctuation:
#     stringi= stringi.replace(i, '')

stringi= stringi.replace("\t", '')
stringi= stringi.replace("\n", '')
stringi= stringi.replace("-", '')
print (stringi)
for i in range(len(stringi)):
    print(stringi[i])


# В некоторой стране используются купюры достоинства 1, 2, 4, 8, 16, 32 и 64 единицы.
# Как наименьшим количеством купюр можно расплатиться за товар стоимостью в N единиц (указать количество каждой из купюр).