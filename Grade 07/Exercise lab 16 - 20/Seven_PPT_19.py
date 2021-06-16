"""
Ex 19.

Create a function that will take in a Boolean and 2 integers. If the boolean is True, multiply them, if the Boolean is false, divide them.
"""

def Boolean_and_2_ints(Bool, int1, int2):
  if(Bool):
    return int1*int2
  else:
    return int1/int2

print(Boolean_and_2_ints(False,6,3))