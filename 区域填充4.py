#!/usr/bin/python
#coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5 * np.pi, 1000)

y1 = np.sin(x)
y2 = np.sin(2 * x)

plt.plot(x, y1, c = "g")
plt.plot(x, y2, c = 'r')

# interpolate 自动填充空白，当x取得离散点差距较大时，
# 显示的时候两个函数之间的区域可能有空白存在，interpolate 就是用来填充这部分区域
plt.fill_between(x, y1, y2, where= y1 >= y2, facecolor = "blue", interpolate= True)
plt.fill_between(x, y1, y2, where= y2 > y1, facecolor = "yellow", interpolate= True)

plt.show()