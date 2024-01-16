import os
import random

soted_l = []
ready = []

with open('solve.txt','w') as opener:
    opener.write('')

def generator():
    allint = []
    a,b,c,d = random.randint(1,10), random.randint(1,10),random.randint(1,10),random.randint(1,10)

    allint.append(a)
    allint.append(b)
    allint.append(c)
    allint.append(d)
    with open('solve.txt','a+') as writer:
        writer.write(f'{a}{b}{c}{d}')


def sorter():
    listo = []

    with open('solve.txt','r') as reader:
        rr = reader.read()
        for i in rr:
            listo.append(int(i))
        

    def intersection(n):
        lenn = range(0,len(n))

        for i in lenn:
            value = n[i]

            while n[i-1] > value and i > 0:
                n[i],n[i-1] = n[i-1],n[i]
                i = i - 1
        ready.append(n)
        print(ready)
        with open('sorted_log.txt','a+') as logger:
            logger.write(f'Listed: {n}\n')
    intersection(listo)
    print(listo)

while True:

    sorter()
    generator()