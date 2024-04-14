import random
def qsort(arr):
    if len(arr)<2:
        return arr
    cursor=arr[0]
    less=[i for i in arr[1:] if i<=cursor]
    greater=[i for i in arr[1:] if i>cursor]
    return qsort(less)+[cursor]+qsort(greater)
arrx=[random.randint(-100,100) for i in range(10)]
print(f"Result: {qsort(arrx)}")