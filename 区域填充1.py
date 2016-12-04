#!/usr/bin/python
#coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5 * np.pi, 1000)

y1 = np.sin(x)
y2 = np.sin(2 * x)

plt.plot(x, y1, label = "$ y = sin(x) $")
plt.plot(x, y2, label = "$ y = sin(2 * x) $")
plt.legend(loc = 3)

plt.show()