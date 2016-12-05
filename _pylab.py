#!/usr/bin/python
#coding: utf-8

from pylab import *

x = arange(0, 10, 1)
y = randn(len(x))

title("pylab")
plot(x, y)
show()