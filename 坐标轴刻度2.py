#!/usr/bin/python
#coding: utf-8

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import datetime

fig = plt.figure()

start = datetime.datetime(2016, 1, 1)
end = datetime.datetime(2017, 1, 1)
# 设置日期的间隔为1
delta = datetime.timedelta(days= 1)

# 生成一个matplotlib可以识别的日期对象
dates = mpl.dates.drange(start, end, delta)
# y轴产生随机数
y = np.random.rand(len(dates))

# 获取当前的坐标
ax = plt.gca()
# 使用plot_date绘制日期图像
ax.plot_date(dates, y, linestyle = "-", marker = ".")

# 设置x轴显式的数量
# 由于x轴是字符串，所以不能够设置刻度
# plt.locator_params("x", nbins = 5)

# 设置日期的显示格式
date_format = mpl.dates.DateFormatter("%Y-%m-%d")
ax.xaxis.set_major_formatter(date_format)

# 日期的排列根据图像的大小自适应
fig.autofmt_xdate()

plt.show()