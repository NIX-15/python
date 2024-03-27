rooms=(int(input("How many rooms?: ")))
i=1
while i<=rooms:
    print("Room",i)
    students=(int(input("How many students in this room? ")))
    print((students+1)//2,"desk(s) for Room",i)
    i+=1