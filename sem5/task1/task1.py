def fib(i):
    if i>2:
        return fib(i-1)+fib(i-2)  
    return 0 if i==1 else 1
print(fib(26))
    
#0 1 1 2 3 5 8 13 21 34
#1 2 3 4 5 6 7 8  9  10