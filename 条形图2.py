#!/usr/bin/python
#coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

x = np.random.randint(10, 50, 20)
y1 = np.random.randint(10, 50, 20)
y2 = np.random.randint(10, 50, 20)

r = 0.5

plt.bar(left= x, height= y1, width= 0.5, color = "red")
# 通过设置 left 来设置并列显示
plt.bar(left = x + r, height = y2, width = 0.5, color = "blue")
plt.show()