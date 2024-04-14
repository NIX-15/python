def nocycle(n):
    if n<k*2:
        print(n+1, end=" ")
        return nocycle(n+1)
k=4
nocycle(k)