max_=-1
game_d={1:'Ivan',-1:'Petr'}
flag=1
n=abs(int(input("Введите число:")))
while n!=0:
    if n>max_:
        max_=n
    flag*=-1
    n=abs(int(input("Введите число:")))
if max_==-1:
    print("No Contest!")
else:
    print(f"Maximum: {max_}, Winner: {game_d[flag]}")
