print('!')
a="hello"
b='world'
#print(a,b)
print(type("!"))

s='hello "man"'
print(s)


a=3
b=11
c=2024

#print(a,b,c)
print(a,"-",b,'-',c)
print('{}-{}-{}-{}'.format(a,b,c,"master!"))
print(f'first-{a} second-{b} and third-{c}')

#a=input()

#b=input()

#c=input()

#print(c+a+b)
#print((a+b)*int(c))
#print(str(a+b+c)*3)
#print(float(int(c)/7))

n="3.14"
print(float(n)*2980237.73)
m="3.14"
print(int(float(m)))

#print('input n')
#n=float(input())
#print("input m")
#m=int(input())
#o=round(n/m,6)
#print(o)

i=2
print(i)
i**=3
print(i)
i//=3
print(i)


a=1>4
print(a)
b=4!=5 and 4>1
print(b)


e="qwe"
f='qwe'
print(e==f)

a=int(input())
b=int(input())
if a>b:
    print(a)
elif a==b:
    print(f'numbers a - {a} and b - {b} are equal!')
else:
    print(b)