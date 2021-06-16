"""
Ex 28.

Add to the preivous class another variable age and a corresponding function, change_age to change the age.
"""

class animal:
  animal_type = ""
  age = 0

  def change_type(self,str_in):
    self.animal_type = str_in

  def change_age(self,int_in):
    self.age = int(int_in)