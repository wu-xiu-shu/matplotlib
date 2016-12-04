#!/usr/bin/python
#coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

fig, ax = plt.subplots()

# 圆的圆心坐标
xy1 = np.array([0.2, 0.2])
# 矩形的左下角
xy2 = np.array([0.1, 0.7])
# 多边形的中心
xy3 = np.array([1.0, 0.2])
# 椭圆的中心
xy4 = np.array([1.0, 0.8])
# 多边形的中心
xy5 = np.array([0.6, 0.6])

# 第二个参数是圆的半径
circle = mpatches.Circle(xy1, 0.1, color = "r")
ax.add_patch(circle)

# 第二个参数和第三个参数是先长后宽
rectangle = mpatches.Rectangle(xy2, 0.2, 0.2, color= "g")
ax.add_patch(rectangle)

# 第二个参数是边数，第三个是距离中心的位置
polygon1 = mpatches.RegularPolygon(xy3, 5, 0.1, color= "y")
ax.add_patch(polygon1)

# 绘制椭圆，第二个参数是椭圆的长直径，第三个是短直径
# 切记，是直径
ellipse = mpatches.Ellipse(xy4, 0.4, 0.2, color= "b")
ax.add_patch(ellipse)

polygon2 = mpatches.RegularPolygon(xy5, 6, 0.2, color= "c")
ax.add_patch(polygon2)

# 设置图形显示的时候x轴和y轴等比例
ax.axis("equal")

# 添加网格
ax.grid()

plt.show()