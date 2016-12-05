#!/usr/bin/python
#coding: utf-8

# 概率分布直方图
# 本例是标准正态分布

import numpy as np
import matplotlib.pyplot as plt

# 设置均值，中心所在点
mean = 0
# 用于将每个点都扩大响应的倍数
sigma = 1

# x中的点分布在 mean 旁边，以mean为中点
x = mean + sigma * np.random.randn(20000)

# hist 设置分组的个数
# normed 是否对y轴数据进行标准化(如果为True，则是在本区间的点在所有的点中所占的概率)
# 如果 normed 为False， 则是显示点的数量
plt.hist(x, bins = 100, color = "red", normed = True,)
# plt.hist(x, bins = 100, color = "red", normed = False,)
plt.show()