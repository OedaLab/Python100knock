import sys
import numpy as np

argvs = sys.argv  # コマンドライン引数を格納したリストの取得
argc = len(argvs) # 引数の個数

print(argvs)
print(argc)
print()
if (argc != 2):   # 引数が足りない場合は、その旨を表示
    print('your input=[%s]' % argvs[0])
    sys.exit()         # プログラムの終了

print('your input=[%s]' % argvs[1])

np.random.seed(int(argvs[1]))
hp = int(np.random.random()*100)
mp = int(np.random.random()*100)
at = np.random.random()*100
de = np.random.random()*100
sp = np.random.random()*100
il = np.random.random()*100
lu = np.random.random()*100


print('HP=%d' %(hp))
print('MP=%d' %(mp))
print('Attack=%.2f' %(at))
print('Deffense=%.2f' %(de))
print('Speed=%.2f' %(sp))
print('Intelligence=%.2f' %(il))
print('Luck=%.2f' %(lu))
