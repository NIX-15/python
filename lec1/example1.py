n=int(input())
flag=True
while flag:
    if abs(n)!=0:
        print (n)
    n-=int(n/abs(n))
else:
    print (n)
flag=False

r=range(3,6)
for i in r:
    print(i)

#line=""
for i in range(7):
    line=""
for j in range(10):
    line+='*'
print(line)

text="deep dark fantasies"
print(text)
print(len(text))
print("Ass" in text)
print(text.upper())
print(text.replace("deep","DEEP"))
#help(range)



text="Thank you, sir!"
print(text[len(text)-1])
print(text[7:])
print(text[2:9])
print(text[9:-2])
print(text[:5:2])