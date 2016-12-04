#!/usr/bin/python
#coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5 * np.pi, 1000)

y1 = np.sin(x)
y2 = np.sin(2 * x)

plt.fill(x, y1, color = "g", alpha = 0.3)
plt.fill(x, y2, color = "b", alpha = 0.3)

plt.show()