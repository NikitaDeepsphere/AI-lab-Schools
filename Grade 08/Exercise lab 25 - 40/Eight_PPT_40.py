"""
Ex 40.

Create and show a pie chart that has 4 randomized sections.
"""

import matplotlib.pyplot as plt
import numpy as np
import random

X = np.array([random.randrange(0,100), random.randrange(0,100), random.randrange(0,100), random.randrange(0,100)])

plt.pie(X)