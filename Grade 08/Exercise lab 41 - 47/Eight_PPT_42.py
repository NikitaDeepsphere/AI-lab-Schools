"""
Ex 42.

Given the array, arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), arrange it so that the first half of the array is on top when printed and the other half is on the bottom
"""

import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr = arr.reshape(2, -1) # 2 is rows and -1 is columns. The -1 makes it so that it decides how many columns automatically 

print(arr)