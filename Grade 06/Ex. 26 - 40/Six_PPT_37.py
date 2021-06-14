"""
Ex 37.

Create 2 functions where one multiplies by 5 and one takes the output of the first one and adds 4 to the output of it.
"""

def times5(num1):
  return num1*5

def plus4(num1):
  return times5(num1)+4