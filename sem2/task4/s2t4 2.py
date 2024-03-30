import random
max,min=0.0,10.0
n=abs(int(input("How many watermelons?: ")))
for i in range(n):
    # mass=abs(float(input("Enter the weight of watermelon")))
    mass=round(random.uniform(1.0, 10.0),2)
    print(mass)
    if mass>max:max=mass
    elif mass<min:min=mass
print('min -',min,'max -',max)