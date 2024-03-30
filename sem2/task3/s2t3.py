import random
MIN_TEMP=-50
MAX_TEMP=50
record = series = 0
n=abs(int(input("Enter the number of days: ")))
for i in range(n):
    temp = random.randint(MIN_TEMP,MAX_TEMP)
    print(f"Day {i+1} - Temperature {temp}")
    if temp>0:
        series+=1
    elif series>record:
        record,series=series,0
    else:
        series=0   
print(record)