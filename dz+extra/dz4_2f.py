arr = [750, 200, 150, 400, 500, 180]
if len(arr)>3:
    arr.append(arr[0])
    arr.insert(0,arr[-2])
    print(arr)
    mymax=arr[0]+arr[1]+arr[2]
    for i in range(2,len(arr)-1):
        if arr[i-1]+arr[i]+arr[i+1]>mymax:
            mymax=arr[i-1]+arr[i]+arr[i+1]
    print(mymax)
else:
    print(arr[0]+arr[1]+arr[2])