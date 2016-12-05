#!/usr/bin/python
#coding: utf-8

# 在同一张图中显示多组箱形图

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(100)
# 用来设置每一组的名字
labels = ["A", "B", "C", "D", "E"]

# 创建5组，每一组有1000个数
data = np.random.normal(size = (1000, 5), loc= 0, scale= 1)

plt.boxplot(data, labels = labels, sym = "o")
plt.show()