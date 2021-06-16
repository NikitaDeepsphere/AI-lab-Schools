"""
Ex 42.

Given a list of integer numbers, return the average value of the numbers
"""

numbers = [10,12,13,14,12,11,15,19,7,6,46] # can be any list, this is just an example
def average(numbers):
  total = 0
  for x in numbers:
    total+=x
  return total/len(numbers)

print(average(numbers))