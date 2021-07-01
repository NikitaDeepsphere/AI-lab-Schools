"""
Ex 16.

Create a function that will find the index of where the first time the character 'e' occurs in a string.

Hint: Use the function .index('e')
"""

str = "Where is there an e here?"

def indexOf(string):
  return str.index('e')

print(indexOf(str))