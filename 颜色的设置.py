#!/usr/bin/python
#coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(10)

# 使用内建的方法
plt.plot(x, color = "g")
# 使用灰色阴影
plt.plot(x + 1, color = "0.5")
# 使用html最常用的16进制表示
plt.plot(x + 2, color = "#FF00FF")
# 使用RGB元组的形式
plt.plot(x + 3, color = (0.1, 0.2, 0.3))

plt.show()