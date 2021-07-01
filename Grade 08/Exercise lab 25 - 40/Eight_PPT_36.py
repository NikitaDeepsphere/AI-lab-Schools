"""
Ex 36.

Now Using the random class in python, create a bar chart with 4 categories, "A" through "D", but randomize each value from 1 to 20.
"""

import numpy as np
import matplotlib.pyplot as plt
import random

X = np.array(["A", "B", "C", "D"])
Y = []
for x in range(0,4):
  Y.append(random.randrange(1,21))


plt.bar(X, Y)