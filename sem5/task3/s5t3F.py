def prosto(n):
    if k<2:
        return 'No! 0 and 1 is not prime'
    if k==2:
        return "Yes! 2 is prime."
    if k>2 and k%2!=0:
        for i in range(3,int(n**0.5+1),2):
            if n%i==0:
                return 'No'
        return 'Yes'
    else:
        return "No. Number is even"
k=abs(int(input("Введите число: ")))
print(prosto(k))