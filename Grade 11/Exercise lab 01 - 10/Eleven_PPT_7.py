""""
Ex. 7

Program Description: The objective of this program is to create a constructor for the “Decryptor” class which does not input anything.
"""

class Student:
  name = ""
  id_number = 0
  age = 0

  def __init__(self, name, id_number, age):
    self.name = name
    self.id_number = id_number
    self.age = age
  
  def get_name(self):
    return self.name
  
  def get_id(self):
    return self.id_number

  def get_age(self):
    return self.age


