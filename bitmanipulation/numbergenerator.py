import random

f = open('input04.txt', 'w')
f.write(str(15001) + '\n')

l = []

for i in range(5000):
    x = random.randint(1,1000)
    l.append(x)
    l.append(x)
    l.append(x)

l.append(987652)

random.shuffle(l)


for i in l:
    f.write(str(i) + '\n')

f.close()
