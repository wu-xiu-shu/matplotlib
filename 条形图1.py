#!/usr/bin/python
#coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(10)
y = np.random.randint(10, 30, 10)

# 画竖直方向的条形图
# plt.bar(left= x, height= y, width= 0.5, color = "red")

# 画水平方向的条形图
# 注意两句话中有区别的地方
# plt.bar(left = 0, bottom= x, width= y, height= 0.5, color = "red",  orientation = "horizontal")
# 或者使用barh函数，不需要显示声明orientation = "horizontal"
plt.barh(left = 0, bottom= x, width= y, height= 0.5, color = "red")
plt.show()