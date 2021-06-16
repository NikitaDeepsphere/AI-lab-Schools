"""
Ex 32.

Add to the Calculator class a constructor that takes in self, 2 numbers, and a string for operation
"""

class Calculator:
   num1 = 0
   num2 = 0
   operation = ""

   def __init__ (self, num1, num2, operation):
     self.num1 = int(num1)
     self.num2 = int(num2)
     self.operation = operation