# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# Make some data
x  = np.arange(0.0, 2.0, 0.01)
# 3 functions
y1 = x
y2 = x*x
y3 = x*x*x

# Create plots with labels
fig, ax = plt.subplots()
ax.plot(x, y1, 'b', label='linear')
ax.plot(x, y2, 'g', label='quadratic')
ax.plot(x, y3, 'r', label='cubic')

# Set title, x lable and y label
ax.set_title('simple plot')
ax.set_xlabel('x label')
ax.set_ylabel('y label')

# Set legend
legend = ax.legend(loc='upper left', shadow=True, fontsize='smaller')
legend.get_frame().set_facecolor('#FFFFFF')

plt.show()