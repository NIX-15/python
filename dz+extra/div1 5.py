import random
#num=random.randint(1,100)
num=16
div=[1,num]
result=[]
summm=8
print(num,'\n')
for i in range(2,num):
    if num%i==0:
        div.insert(len(div)-1,i)
#        print (i)
for i in div:
    print(i, end = ' ')
for i in div[:len(div)//2+len(div)%2]:
    for j in div:
        if i+j==summm and i*j==num:
            result.extend((i,j))
print('\n')
for i in result:
    print(i, end = ' ')