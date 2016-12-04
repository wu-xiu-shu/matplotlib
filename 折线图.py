#!/usr/bin/python
#coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

# linspace 用于生成等区间的一组数
# 本例中生成从 -10 到 10 的5个数
x = np.linspace(-10, 10, 5)

y = x ** 2

# 使用 plot 绘制折线图
# linestyle 设置线的类型，
# 需要注意的 linestyle，c，marker
plt.plot(x, y, linestyle = "--")
plt.show()