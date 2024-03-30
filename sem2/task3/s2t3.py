flag=False
while(not flag):
    n=abs(int(input("Enter the number of days:")))
    if(n>10):
        print("error")
    else:
        flag=True
c=0
max=0
i=1
while(i<=n):
    while(flag):
        t=int(input("Enter the temperature"))
        if(t>50 or t<-50):
            print("Temperature error!")
        else:
            flag=False
    print("day",i,"temperature",t)
    if(t>0):
        c+=1
        if(c>max):
            max=c
    else:
        if(c>max):
            c=0
    i+=1
    flag=True
print(max)