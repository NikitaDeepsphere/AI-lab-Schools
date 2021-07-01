"""
Ex 26.

Plot a line from (1,1) to (8, 8)
"""
import matplotlib.pyplot as plt
import numpy as np

x = range(1, 9)
y = [i for i in x]

plt.plot(x, y)
plt.show