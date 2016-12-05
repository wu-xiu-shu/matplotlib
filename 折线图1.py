#!/usr/bin/python
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

# 设置x的取值范围，在这个范围里面绘制图形，
# 要注意，本例中取得是2个循环，一个np.pi表示的是绘制的一个循环的一半
x = np.arange(0, 4 * np.pi, 0.01)
y1 = np.sin(x)
y2 = np.cos(x)


# 设置y轴的范围
plt.ylim(-1.5, 1.5)

# 设置x轴和y轴的标签
plt.xlabel(u"x")
plt.ylabel(u"y")
# 设置标题
plt.title(u"Example")
# label设置线的名称
plt.plot(x, y1, label = u"$y = sin(x)$")
plt.plot(x, y2, label = u"$y = cos(x)$")
# 显示图示
plt.legend()
# 显示图片
plt.show()
# 保存图片
plt.savefig("text.jpg")

# 可以添加一些东西装饰一下。
# plt.xlabel（“x轴标签”）
# plt.ylabel("y轴标签")
# plt.title("图像标题")
# plt.xlim(0,5)     在画好的图形中选取x范围内的图形片段。
# plt.ylim(0,5)     y片段
# plt.plot(x,y,linewidth=4)    设置线的宽度
# plt.plot(x,y,"g字符")     g代表绿色 后面的字符表示线的种类。如虚线，点线等
# {y:黄色   b:黑色  c:灰色  默认为蓝色}