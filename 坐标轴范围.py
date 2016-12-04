#!/usr/bin/python
#coding: utf-8

import numpy as np 
import matplotlib.pyplot as plt 

x = np.arange(-101, 101, 1)

plt.plot(x, x ** 2)
# 查看此时的x轴的最大值和最小猪和y轴的最大值最小值
# print plt.axis()
# 设置四个最值，列表传入
plt.axis([-100, 100, 0, 10000])

# 查看此时x轴的最大值和最小值
# print plt.xlim()
# 设置最大值和最小值(可以两个都设置，也可以只设置一个，只设置一个的时候要显式声明)
plt.xlim(-200, 200)
# 显式指定
# plt.xlim(xmin = -200, xmax = 200)
plt.xlim(xmin = -100)
plt.xlim(xmax = 100)

# 还有专门针对于y轴而言的ylim，xlim具备的方法ylim都具备，不再描述

plt.show()