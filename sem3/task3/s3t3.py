import random
size_1=9
dict1 = {random.choice('abcdefghijklmno'):random.randint(-10,10) for _ in range(size_1)}
# print(len(dict1))
print(dict1)
temp1=len(dict1)
for x in dict1:
    #print(x,dict1[x])
    y=x
    for y=x in dict1:
        print(y)
        if dict1[y]==dict1[x] and y!=x:
            print("LOL")
            temp1-=1
print(temp1)            
# new_set = set(dict1.values()) 
# print(new_set)
# print(len(new_set))  