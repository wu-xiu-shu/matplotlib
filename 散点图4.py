#!/usr/bin/python
#coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

n = 1000
x = np.random.rand(n)
y = np.random.rand(n)
colors = np.random.rand(n)
areas = np.pi * (15 * np.random.rand(n)) ** 2

plt.scatter(x, y, c = colors, s = areas, alpha = 0.5)

plt.show()
