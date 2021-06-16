"""
Ex 31.

Using user input, create a basic calculator that will add or subtract 2 numbers the user passes in. If the user passes in the numbers 1 , 2 and then types in -, then the output should be 1-2, or -1. If the user types in 3,4 and then +, the output should be 3+4, or 7.
"""

num1 = int(input("What is the first number:"))
num2 = int(input("What is the second number:"))
operation = input("What is the desired operation (- or +):")

print() #This is just so there is a space
if(operation == "-"):
  print(num1 - num2)
elif(operation == "+"):
  print(num1+num2)
else:
  print("Not Valid Operation Input")