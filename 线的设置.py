#!/usr/bin/python
#coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(10)

plt.plot(x, "--")
plt.plot(x + 1, "-")
plt.plot(x + 2, "-.")
plt.plot(x + 3, ":")
plt.show()