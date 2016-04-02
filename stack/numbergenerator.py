import random

f = open('input05.txt', 'w')
f.write(str(10000) + '\n')

for i in range(10000):
    f.write(str(random.randint(1, 100)) + '\n')

f.close()
