def fib(i):
    while i>2:
        return fib(i-1)+fib(i-2)  
    if i==1:
        return 0
    elif i in [2]:
        return 1    
print(fib(10))
    
#0 1 1 2 3 5 8 13 21 34
#1 2 3 4 5 6 7 8  9  10