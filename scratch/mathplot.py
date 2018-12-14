# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 17:00:47 2016

@author: richard.dewolff
"""

import matplotlib.pyplot as plt
# Generate a sequence of integers
x = np.arange(20)
# create a second array using sinus
y = np.sin(x)
# The plot function makes a line chart of one array against another
plt.plot(x, y, marker="x")