#!/usr/bin/python
#coding: utf-8
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt

font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)

plt.xlabel(u"电压差(V)", fontproperties=font)
plt.ylabel(u"介质损耗角差(度)", fontproperties=font)
plt.title(u"介质损耗角和荷电状态SOC关系图", fontproperties=font)
plt.show()