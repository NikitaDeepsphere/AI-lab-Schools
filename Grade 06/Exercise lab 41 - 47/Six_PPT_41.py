"""
Ex 41.

Given a list of integer numbers, return the amount of numbers in that list that are even.
"""

numbers = [1,2,3,4,5,6,7,8] # can be any list, this is just an example
def count_evens(numbers):
  count = 0
  for x in numbers:
    if x % 2 == 0:
      count+=1
  return count