n=int(input("Enter the number: "))
if(n<0):
    print("Error! Negative number")
else:
    i=1
    result=1
    while(i<=n):
        result*=i
        i+=1
    print(result)