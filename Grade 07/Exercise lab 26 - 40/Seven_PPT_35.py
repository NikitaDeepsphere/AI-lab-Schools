"""
Ex 35.

Add to the Calculator class a calculate function that depending on the operation, will call one of the other functions and return the output. Ex. if operation is "*", then it will return self.multiply()
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

   def subtract(self):
     return self.num1-self.num2

   def multiply(self):
     return self.num1*self.num2

   def divide(self):
     return self.num1/self.num2
   
   def calculate(self):
     if(self.operation == "*"):
       return self.multiply()

     elif(self.operation == "/"):
       return self.divide()
     
     elif(self.operation == "-"):
       return self.subtract()

     else:
      return self.add()

calc = Calculator(2,3,"-")
print(calc.calculate())