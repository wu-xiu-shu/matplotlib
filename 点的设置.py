#!/usr/bin/python
#coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 6)

# 在画多条线段的时候，如果说对颜色没有特别的要求，其实没必要进行指定，
# matplotlib会自动的设置颜色的类型，便于区分

# marker 显式指定的话，画出的是线段，
# 如果不显式指定，画出的是给定的类型,一些点，比如使用 _(下划线) 的话，
# matplotlib内部也会分辨出是marker对象

plt.plot(x - 1, "o")
plt.plot(x, marker = "o")
plt.plot(x + 1, marker = "1")
plt.plot(x + 2, marker = "_")
plt.plot(x + 3, marker = "8")
plt.show()