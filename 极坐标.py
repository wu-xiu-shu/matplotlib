#!/usr/bin/python
#coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

# print plt.style.available
plt.style.use("ggplot")

r1 = np.arange(1, 6, 1)
# 生成5个数，每个数都是5
r2 = np.empty(5)
r2.fill(5)

# 生成9个数，每个数都是5
r3 = np.empty(9)
r3.fill(5)
# print len(r3)

r4 = np.empty(7)
r4.fill(5)

theta1 = np.arange(0, 2 * np.pi + 1, np.pi /2)
# 八边形中每一个顶点在极坐标中所占的角度
theta2 = np.arange(0, 2 * np.pi + 0.00000001, np.pi / 4)
# print len(theta2)
theta3 = np.arange(0, 2 * np.pi + 0.000000001, np.pi /3)

# 投影成极坐标
ax1 = plt.subplot(221, projection = "polar")
ax1.plot(theta1, r1, color = "r", linewidth = 3)
ax1.grid(True)

ax2 = plt.subplot(222, projection = "polar")
ax2.plot(theta1, r2, color = "g", linewidth = 3)
ax2.grid(True)

ax3 = plt.subplot(223, projection = "polar")
ax3.plot(theta2, r3, color = "b")
ax3.grid(True)

ax4 = plt.subplot(224, projection = "polar")
ax4.plot(theta3, r4, color = "y", linewidth = 3)
ax4.grid(True)

plt.show()