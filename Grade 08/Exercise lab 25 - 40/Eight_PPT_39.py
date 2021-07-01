"""
Ex 39.

Create and show a pie chart that has 4 equal sections.
"""

import matplotlib.pyplot as plt
import numpy as np

X = np.array([25, 25, 25, 25])

plt.pie(X)