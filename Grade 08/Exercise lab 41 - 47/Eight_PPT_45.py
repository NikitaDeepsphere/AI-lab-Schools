"""
Ex 45.

Create a random array with floats from 0 to 1. Give this array 4 rows and 6 columns.

Hint: use np.random.random(rows,columns)
"""

import numpy as np

rand_arr = np.random.random([4,6])

print(rand_arr)