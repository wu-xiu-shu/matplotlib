#!/usr/bin/python
#coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()

ax = fig.add_subplot(111)
ax.set_xlim([1, 10])
ax.set_ylim([1, 10])

ax.text(7, 3, r"$ \alpha_i \beta_j \pi \lambda \omega $", size = 25)
# 如果诸如sin这种，前面不加\也能够显示，但是字体会不一样，
# 加上以后sin就变成了数学函数，不然的话会当做普通的文本进行处理
ax.text(2, 3, r"$ \sin(0) = \cos(\frac{\pi}{2}) $", size = 25)
# ^\infty上方显示无穷大
ax.text(3, 5, r"$ \Re \prod_{i = \alpha_{i+1} }^\infty \alpha_i \sin(2\pi f x_i) $", size = 25)

ax.text(2, 7, r"$ \lim_{ x \rightarrow y }\frac{1}{x^3} $", size = 25)
# 默认的是2，所以第二个没有加[2]
ax.text(7, 7, r'$\sqrt[4]{x} = \sqrt{y}$', size = 25)

plt.show()