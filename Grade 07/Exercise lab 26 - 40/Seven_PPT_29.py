"""
Ex 29.

Add to the previous class another function, get_type that will print the value of animal type
"""

class animal:
   animal_type = ""
   age = 0

   def change_type(self,str_in):
     self.animal_type = str_in

   def change_age(self,int_in):
      self.age = int(int_in)
   
   def get_type(self):
     print(self.animal_type)