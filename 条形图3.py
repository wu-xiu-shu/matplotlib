#!/usr/bin/python
#coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

x = np.random.randint(10, 50, 20)
y1 = np.random.randint(10, 50, 20)
y2 = np.random.randint(10, 50, 20)

# 设置y轴的显示范围
plt.ylim(0, 100)

plt.bar(left = x, height = y1, width = 0.5, color = "red", label = "$y1$")
# 设置一个底部，底部就是y1的显示结果，y2在上面继续累加即可。
plt.bar(left= x, height= y2, bottom= y1, width= 0.5, color = "blue", label = "$y2$")

plt.legend()

plt.show()