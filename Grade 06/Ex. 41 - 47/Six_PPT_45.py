"""
Ex 45.

Given a list of integer numbers, find the sum of all numbers that are either odd or less than 100
"""

numbers = [12,145,14,122,142,2,3154,132,132,242,1245,235,123] # can be any list, this is just an example
def odd_or_hundred(numbers):
  total=0
  for x in numbers:
    if(x%2 == 1 or x<100):
      total+=x
  return total

print(odd_or_hundred(numbers))