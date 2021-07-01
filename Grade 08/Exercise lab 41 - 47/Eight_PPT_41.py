"""
Ex 41.

Given the array, arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), extract all odd numbers from the array.
"""

import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr = arr[arr % 2 == 1]

print(arr)