#!/usr/bin/python
#coding: utf-8

# 不相关

import matplotlib.pyplot as plt
import numpy as np

# # 产生100到200的10个随机整数
# height = np.random.randint(100, 200, 10)
# width = np.random.randint(100, 130, 10)
#
# # 绘制图形
# plt.scatter(height, width)
# # 显示图形
# plt.show()

x = np.random.randn(1000)
y = np.random.randn(1000)

# x指x轴
# y指y轴
# s设置显示的大小，指的是面积
# c设置显示的颜色
# marker设置显示的形状,所有的类型：http://matplotlib.org/api/markers_api.html?highlight=marker#module-matplotlib.markers
# alpha 设置点的透明度， 如果点特别多的时候可以观察点在什么地方集中
plt.scatter(x, y, s= 100, c= "r", marker= "v", alpha= 0.5)
plt.show()