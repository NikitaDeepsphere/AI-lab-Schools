"""
Ex 17.

Create a function that will combine a list of strings and ouput a sentence of the strings in the list. Example: if list = ["This", "is", "a", "test"], then the output would be "This is a test"
"""

check = ["This", "is", "a", "test"]
def sentence(check):
  output = ""
  for x in check:
    output = output + x + " "
  return output

print(sentence(check))