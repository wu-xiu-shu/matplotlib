#!/usr/bin/python
#coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def func(x):
    return (x ** 3) / 3.0

fig, ax = plt.subplots()

x = np.arange(-10, 11, 1)
y = func(x)

a = -8
b = 8
ax.set_xticks([a, b])
ax.set_xticklabels([r"$ a $", r"$ b $"])

ix = np.linspace(a, b)
iy = func(ix)
ixy = list(zip(ix, iy))
verts = [(a, 0)] + ixy + [(b, 0)]
polygon = mpatches.Polygon(verts, facecolor= "0.8", edgecolor= "0.2")
ax.add_patch(polygon)

plt.plot(x, y, color = "r", linewidth = 2)

x_math = (a + b) * 0.5
y_math = 0

plt.text(x_math, y_math, r"$ \int_a^b \frac{1}{3} x^3 dx$", fontsize = 20, horizontalalignment = "center")

plt.figtext(0.9, 0.05, r"$ x $")
plt.figtext(0.125, 0.92, r"$ y $")

x = np.arange(-10, 11, 1)
y1 = x * 0
# print x
# print y1
# 画出 y = 0 的函数图像
plt.plot(x, y1, color = "g", linewidth = 2)

plt.show()