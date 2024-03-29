flag=False#пока не убедились в правильности ввода
while(not flag):
  fhead=int(input("Victor goes to Wagon from head #"))
  if(fhead<1 or fhead>50):
    print("Error!")
  else:
    print(fhead)
    flag=True
flag=False
edge=""
if(fhead==1):
  while(not flag):
    onboard=int(input("Once in the wagon, Victor sees its on-board number:"))
    if(fhead==onboard):
      print("Lack of information!")
      flag=True
    elif(onboard>1 and onboard<51):
      print("The train consists",onboard,"wagons")
      flag=True
    else:
      print("Invalid Input!")
else:
  while(not flag):
    print("Is this wagon the last?:")
    edge=(input())
    if(edge.lower()=='yes'):
      print("The train consists",fhead,"wagons")
      flag=True
    elif(edge.lower()=="no"):
      while(not flag):
        onboard=int(input("Once in the wagon, Victor sees its on-board number:"))
        if(onboard>1 and onboard<51):
          flag=True
        else:
          print("Invalid onboard input")
    else:
      print("Type yes or no")
      flag=False
  if(edge.lower()=="no" and fhead==onboard):
    print("Lack of information")
    flag=True
  elif(edge.lower()=="no" and fhead!=onboard):
    print("The train consists",fhead+onboard,"wagons")
    flag=True
  else:
    frag=True