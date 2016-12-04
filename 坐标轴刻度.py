#!/usr/bin/python
#coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10, 1)

plt.plot(x, x)

# 获取当前的坐标轴
ax = plt.gca()
# 设置把x轴和y轴都平均分成20份
# ax.locator_params(nbins = 20)
# 指定需要设置的x轴或y轴的刻度
# ax.locator_params("x", nbins = 20)
# 设置y轴
ax.locator_params("y", nbins = 5)

# 上面是采用面向对象的方式运行的，如果要在交互式窗口进行对坐标轴进行修改并不能成功

# 下面是采用pyplot的方式
plt.locator_params("x", nbins = 5)

plt.show()