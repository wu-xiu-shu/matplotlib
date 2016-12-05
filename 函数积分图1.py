#!/usr/bin/python
#coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def func(x):
    return -(x - 2) * (x - 8) + 40

x = np.linspace(0, 10)
y = func(x)

a = 2
b = 9

fig, ax = plt.subplots()
# 设置x轴要显示的坐标(官网)
ax.set_xticks([a, b])
# y轴显示
ylist = np.arange(0, 60, 10)
ax.set_yticks(ylist)
# 设置x轴显示的标签为a和b，用公式的形式显示
ax.set_xticklabels([r'$ a $', r'$ b $'])

ix = np.linspace(a, b)
iy = func(ix)
# 打包
ixy = list(zip(ix, iy))
verts = [(a, 0)] + ixy + [(b, 0)]
# edgecolor 设置边框的颜色深度
# facecolor 设置内部的颜色深度
polygon = mpatches.Polygon(verts, facecolor= "0.8", edgecolor= "0.2")
ax.add_patch(polygon)

# 设置x和y所在的位置
# 前面的两个小数是把x轴或者y轴当做从0到1，然后获得的相对值
plt.figtext(0.9, 0.05, "$ x $")
plt.figtext(0.1, 0.9, "$ y $")

plt.plot(x, y, color = "r", linewidth = 2)

# 数学公式显示的位置
x_math = (a + b) * 0.5
y_math = 20

# horizontalalignment 通过给定的x和y的值设置居中显示
plt.text(x_math, y_math, r"$ \int_a^b (-(x - 2) * (x - 8) + 40) dx$", fontsize = 20,horizontalalignment = "center")
plt.ylim(ymax = 60)
plt.show()