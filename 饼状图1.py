#!/usr/bin/python
#coding: utf-8

# 饼状图: 显示一个系列中各项的大小以及各项所占总和的比例
# 饼状图中的数据点显示为整个饼状图的百分比

import numpy as np
import matplotlib.pyplot as plt

labels = ["A", "B", "C", "D"]
facts = [25, 40, 20, 15]
explode = [0, 0.03, 0, 0.03]

# 设置显示的是一个正圆，长宽比为 1:1
plt.axes(aspect = 1)

# x为数据, 根据数据在所有数据中所占的比例显示结果
# labels设置每个数据的标签
# autoper 设置每一块所占的百分比
# explode 设置某一块或者很多块突出显示出来， 由上面定义的explode数组决定
# shadow 设置阴影，这样显示的效果更好
plt.pie(x = facts, labels = labels, autopct = "%.0f%%", explode= explode, shadow= True)
plt.show()