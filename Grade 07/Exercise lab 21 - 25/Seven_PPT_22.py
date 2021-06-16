"""
Ex 22.

Create a function that will return the first half of a string (can be a word or sentence)
"""

str1 = "Half of this sentence is"
def half(string):
  return string[:int(len(string)/2)]

print(half(str1))