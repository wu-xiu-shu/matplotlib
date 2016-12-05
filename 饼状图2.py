#!/usr/bin/python
#coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

labels = ["SH", "BI", "SZ", "GD"]
facts = [20, 10, 30, 40]
explode = [0, 0, 0.02, 0]

plt.axes(aspect = 1)

# 练习要求
# 绘制饼状图，突出显示SZ，百分比精确到小数点后一位，有阴影

plt.pie(x = facts, labels = labels, explode= explode, shadow= True)
plt.show()