from random import randint as rand
listik=[rand(-100,100) for _ in range(6)]
print(listik)
num1=int(input("enter the number: "))
mindist=[0,abs(num1-listik[0])]
for i in range(1,len(listik)):
    dist=abs(listik[i]-num1)
    if dist<mindist[1]:
        mindist=[i,dist]
print(mindist)