import random
MAX_WEIGHT=1.0
MIN_WEIGHT=10.0

min_a=MAX_WEIGHT
max_a=MIN_WEIGHT
n=abs(int(input("How many watermelons?: ")))
for _ in range(n):
    # mass=abs(float(input("Enter the weight of watermelon")))
    mass=round(random.uniform(MIN_WEIGHT, MAX_WEIGHT),2)
    print(mass, end=" ")
    if mass>max_a:max_a=mass
    elif mass<min_a:min_a=mass
print(f"\n\nmin - {min_a}\nmax - {max_a}")