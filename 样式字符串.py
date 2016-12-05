#!/usr/bin/python
#coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(10)

plt.plot(x, "g8:")
plt.plot(x + 1, "b4--")
plt.plot(x + 2, "cH-.")
plt.plot(x + 3, "kH-")
plt.plot(x + 4, "ro-")
plt.plot(x + 5, "y3--")

plt.show()