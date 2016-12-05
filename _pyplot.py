#!/usr/bin/python
#coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10, 1)
y = np.random.randn(len(x))

plt.title("pyplot")

plt.plot(x, y)
plt.show()