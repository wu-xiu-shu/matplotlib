#!/usr/bin/python
#coding: utf-8

# 双变量的直方图，可以用来探索双变量的联合分布

import numpy as np
import matplotlib.pyplot as plt

x = np.random.randn(2000) + 2
y = np.random.randn(2000) + 3

plt.hist2d(x, y, bins = 40)
plt.show()