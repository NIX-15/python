import random
size_,maxlen=6,0
list1=[random.randint(-10,10) for i in range(size_)]
print(list1)
for i in range(size_-1):
    if list1[i+1]>list1[i]:
        maxlen+=1
        print(list1[i+1],">",list1[i])
print(f"Result: {maxlen} elements!")