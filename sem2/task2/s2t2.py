n=abs(int(input("input the number: ")))
fib,next_fib = 0,1
i=1
print("f","i")
while fib<n:
  print(fib,i) 
  fib,next_fib = next_fib,fib+next_fib
  i+=1
#print("Solved! ",n,"is #",i,"in Fibonacci series" if next_fib==n else -1)
if fib==n:
  print("Solved! ",n,"is #",i,"in Fibonacci series")
else:
  print(-1)