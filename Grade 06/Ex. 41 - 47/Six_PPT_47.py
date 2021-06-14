"""
Ex 47.

A fibonnaci number is a number created by the sum of the previous 2 numbers starting at 0 and 1. The first 5 fibbonaci numbers are 0,1,1,2,3. Create a function that finds the nth fibbonaci number.
"""

def Fibonacci(n):
  int1 = 0 #creating first 2 numbers
  int2 = 1

  temp = int1 #adding numbers to get next numbers and slidng down number 2 into number1
  int1 = int2
  int2+=temp

  if n < 0:
        print("Not Possible")
  elif n == 0:
        return 0
  elif n == 1 or n == 2:
        return 1
  else:
    return Fibonacci(n-1) + Fibonacci(n-2) #This is an advanced technique called recursion which is used to loop a function within itself.
print(Fibonacci(15))