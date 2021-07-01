"""
Ex 46.

Using the same code from Ex. 45, round each number to 3 decimal places.
"""
import numpy as np

rand_arr = np.random.random([4,6])
np.set_printoptions(precision=3)

print(rand_arr)