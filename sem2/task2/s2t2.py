n=abs(int(input("input the number: ")))
fib,next_fib = 0,1
i=1
print("f","i")
while fib<n:
  print(fib,i)
  fib,next_fib = next_fib,fib+next_fib
  i+=1
print(f"Solved! {n} is #{i} in Fibonacci series" if fib == n else -1)