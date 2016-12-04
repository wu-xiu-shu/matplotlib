#!/usr/bin/python
#coding: utf-8

# 面向对象的方式(没有交互的效果)

import numpy as np 
import matplotlib.pyplot as plt 

x = np.arange(0, 21)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, x * 2)
# 使用面向对象的方式显示网格
ax.grid(True, color = "r")

plt.show()