"""
Ex 22.

Add Each value in the list (From Ex 21) to the corresponding value from: add = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
"""

int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in range(len(int_list)):
  int_list[x]*=12
add = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
for x in range(len(int_list)):
  int_list[x] = (int_list[x] + add[x])