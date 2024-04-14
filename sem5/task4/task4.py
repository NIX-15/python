def nocycle(n):
    if n<k*2:
        print(3*k-n, end=" ")
        return nocycle(n+1)
k=3
nocycle(k)