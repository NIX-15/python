import random
import shutil
nums=str([random.randint(-10,10) for x in range(random.randint(1,10))])

with open('file2.txt','a') as data1:
    data1.write(str([random.randint(-10,10) for x in range(random.randint(1,10))])+'\n')
    data1.write(str([random.randint(-10,10) for x in range(random.randint(1,10))])+'\n')
    data1.write(str([random.randint(-10,10) for x in range(random.randint(1,10))])+'\n')

data = open('file1.txt','a')
data.writelines(nums+'\n')
data.close()
path = 'file1.txt'
data2=open('file1.txt')
for line in data2:
    print(line)
data2.close()



shutil.copy('file2.txt','lec4')