"""
Ex 21.

Create a function that will take in a string and output the string but with each character doubled. For example: double("Apple") = "AAppppllee"
"""

str1 = "Apple"

def double(string):
  output = ""
  for x in range(len(string)):
    output = output + string[x] + string[x]
  return output

print(double(str1))