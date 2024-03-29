flag=False
while(not flag):
    visok=int(input("Enter the Year:"))
    if(visok<1 or visok>10000):
        print("Wrong Input! Try again!")
    else:
        flag=True
if((visok%4==0 and visok%100!=0) or visok%400==0):
    print("YES.",visok,"is a leap year")
else:
    print("NO.",visok,"is a non-leap year")