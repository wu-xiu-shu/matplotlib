#!/usr/bin/python
#coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10, 1)
y = np.random.randn(len(x))

# 生成一个figure对象
fig = plt.figure()
ax = fig.add_subplot(111)

plt.plot(x, y)

ax.set_title("object oriented")

plt.show()