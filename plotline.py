# 20. matplotlibを使って，y = 3*x**2 - 1のグラフを描画．

import numpy as np
import matplotlib.pyplot as plt

def func(x):
    y = -3 * x**2 - 1
    return y

xmin = -3
xmax = 3
num = 30

x = np.linspace(xmin, xmax, num)
y = func(x)

plt.plot(x, y)
plt.grid()
plt.show()
