#!/usr/bin/python
#coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 11, 1)
y = x * x

plt.plot(x, y)

# 添加注释
# 第一个参数是注释的内容
# xy设置箭头尖的坐标
# xytext设置注释内容显示的起始位置
# arrowprops 用来设置箭头
# facecolor 设置箭头的颜色
# headlength 箭头的头的长度
# headwidth 箭头的宽度
# width 箭身的宽度
plt.annotate(u"This is a zhushi", xy = (0, 1), xytext = (-4, 50),\
             arrowprops = dict(facecolor = "r", headlength = 10, headwidth = 30, width = 20))
# 可以通过设置xy和xytext中坐标的值来设置箭身是否倾斜

plt.show()