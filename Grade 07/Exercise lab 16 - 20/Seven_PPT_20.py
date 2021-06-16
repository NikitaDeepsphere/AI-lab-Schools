"""
Ex 20.

Create a function that will take in 2 integer lists and output a list that multiplies the numbers in each list with each other. Assume the lists are the same length.
"""

check1 = [1,2,3,4,5,6,7,8,9,10]
check2 = [1,2,3,4,5,6,7,8,9,10]

def multiply_lists(l1, l2):
  output = []
  for x in range(len(l1)):
    output.append(l1[x]*l2[x])
  return output

print(multiply_lists(check1,check2))