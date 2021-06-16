"""
Ex 24.

Create a function that will pass in a string that is a sentence, and output a list with each item in the list containg a word from the sentence. Example: toList("Convert this to a list") = ["Convert", "this", "to", "a", "list"]

Hint: Use .split(" ")
"""

str = "Convert this to a list"

def toList(string):
  return string.split(" ")

print(toList(str))