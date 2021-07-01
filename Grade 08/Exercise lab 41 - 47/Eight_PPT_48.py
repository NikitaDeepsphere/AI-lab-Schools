"""
Ex 48.

Using the code from ex 47, format the output so that only the first and last 3 numbers will be shown.
"""

import numpy as np

arr = np.arange(20)
np.set_printoptions(threshold=6)

print(arr)