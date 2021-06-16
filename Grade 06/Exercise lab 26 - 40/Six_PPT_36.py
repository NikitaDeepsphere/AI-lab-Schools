"""
Ex 36.

Create a function similar to the previous that takes in a number and prints out the sum of all the numbers under it including the number itself. For example, sum_under(6) would print out 21.
"""

def sum_under(num1):
  out = 0
  for x in range(num1+1):
    out+=x
  print(out)