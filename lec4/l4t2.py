import random
nums=str([random.randint(-10,10) for x in range(random.randint(1,10))])

with open('file2.txt','w+') as data1:
    data1.write(str([random.randint(-10,10) for x in range(random.randint(1,10))])+'\n')
    data1.write(str([random.randint(-10,10) for x in range(random.randint(1,10))])+'\n')
    data1.write(str([random.randint(-10,10) for x in range(random.randint(1,10))])+'\n')
data = open('file1.txt','a')
data.writelines(nums+'\n')
data.close()