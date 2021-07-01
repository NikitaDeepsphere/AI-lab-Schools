"""
Ex 10.

Given a list of integer numbers, find the range of the list (the maximum - minimum value)
"""

numbers = [12,145,14,122,142,2,3154,132,132,242,1245,235,123] # can be any list, this is just an example
def range(numbers):
  min = numbers[0]
  max = numbers[0] 
  for x in numbers:
    if(x < min):
      min = x
    if(x > max):
      max = x
  return max-min

print(range(numbers))