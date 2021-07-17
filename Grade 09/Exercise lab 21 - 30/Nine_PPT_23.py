"""
Ex 23.

Create the function input that will input 2 numbers, and a operation. Then set the self variables to the ones passed in.
"""

class calculator:
  num1 = 0.0
  num2 = 0.0
  op = ""

  def __init__(self):
    return
  
  def input(self, n1, n2, op):
    self.num1 = n1
    self.num2 = n2
    self.op = op
    return