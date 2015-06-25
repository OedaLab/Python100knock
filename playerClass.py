import sys
import numpy as np

class Character:
    seed = 0
    def __init__(self, seed):
        self.seed = seed

    np.random.seed(seed)
    hp = int(np.random.random()*100)
    mp = int(np.random.random()*100)
    at = np.random.random()*100
    de = np.random.random()*100
    sp = np.random.random()*100
    il = np.random.random()*100
    lu = np.random.random()*100

player = []
NUM = 3
for i in range(NUM):
    player.append(Character(i))

for i in range(NUM):
    print('HP=%d' %(player[i].hp))
    print('MP=%d' %(player[i].mp))
    print('Attack=%.2f' %(player[i].at))
    print('Deffense=%.2f' %(player[i].de))
    print('Speed=%.2f' %(player[i].sp))
    print('Intelligence=%.2f' %(player[i].il))
    print('Luck=%.2f' %(player[i].lu))
    print()
