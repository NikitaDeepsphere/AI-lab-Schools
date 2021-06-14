"""
Ex 46.

Create a function that randomly Displays a numerical 4-digit password using random.randint(range). Remeber to type import random at the top!
"""
import random

def randompassword():
  a = random.randint(0,9)
  b = random.randint(0,9)
  c = random.randint(0,9)
  d = random.randint(0,9)
  return str(a) + str(b) + str(c) + str(d)

print(randompassword())