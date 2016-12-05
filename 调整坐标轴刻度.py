#!/usr/bin/python
#coding: utf-8

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 11, 1)

plt.plot(x, x * 2)
# 获取当前的坐标轴
ax = plt.gca()
# 设置平均分成20格
ax.locator_params(nbins = 5)

plt.show()