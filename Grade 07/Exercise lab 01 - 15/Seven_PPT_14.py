"""
Ex 14.

Given a list of numbers, if anywhere in the list, there are 2 consecutive numbers (list[x] == list[x+1]), return true, else return false.
"""
numbers = [12,145,14,122,142,2,3154,132,132,242,1245,235,123] # can be any list, this is just an example
def consecutive(numbers):
  for x in range(len(numbers)-1):
    if(numbers[x] == numbers[x+1]):
      return True
  return False

print(consecutive(numbers))