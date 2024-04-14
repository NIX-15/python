def binar(a, b):
    ans=""
    while b-a!=0:
        print(a,b)
        while ans not in ['y','n']:
            ans=input(f"Число больше {int((a+b)/2)} (y/n)?").lower()
        return binar(int(1+(a+b)/2),b) if ans=='y' else binar(a,int((a+b)/2))
    return b
print("Ваше число -",binar(1,10000))