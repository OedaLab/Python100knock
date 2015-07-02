import random

f = open('output.csv', 'w')

NUM = 1000

num = []
i = 0
ct = 0
while i<NUM:
    f.write('%d, %d\n'%(ct, i))
    print(ct, i)
    r = random.randint(0, NUM-1)
    flag = 0
    for j in range(i):
        if num[j]==r:
            flag = 1
            break

    if flag==0:
        num.append(r)
        i+=1

    ct += 1

f.close()

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('output.csv', header=None)

plt.plot(df[0], df[1])
plt.show()
