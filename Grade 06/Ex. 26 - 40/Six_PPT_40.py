"""
Ex 40.

Revisting the previous topics, create a 4 function calculator using functions that can add, subtract, multiply and divide. Take in user input like before.
"""

num1 = int(input("What is the first number:"))
num2 = int(input("What is the second number:"))
operation = input("What is the desired operation (- , + , / or *):")

def add(n1, n2):
  return n1+n2

def subtract(n1, n2):
  return n1-n2

def multiply(n1, n2):
  return n1*n2

def divide(n1, n2):
  return n1/n2
  
if(operation == "+"):
  print(add(num1,num2))
elif(operation == "-"):
  print(subtract(num1,num2))
elif(operation == "*"):
  print(multiply(num1,num2))
elif(operation == "/"):
  print(divide(num1,num2))
else:
  print("Invalid Operation")