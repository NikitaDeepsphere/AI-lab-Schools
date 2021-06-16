"""
Ex 33.

Add to the Calculator class a function that will add the 2 numbers.
"""

class Calculator:
   num1 = 0
   num2 = 0
   operation = ""

   def __init__ (self, num1, num2, operation):
     self.num1 = int(num1)
     self.num2 = int(num2)
     self.operation = operation

   def add(self):
     return self.num1+self.num2