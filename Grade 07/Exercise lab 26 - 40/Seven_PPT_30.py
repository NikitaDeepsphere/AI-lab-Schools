"""
Ex 30.

Add to the previous class a constructor that will initialize animal_type and age.

Hint: use def __init__(self,...)
"""
class animal:
   animal_type = ""
   age = 0

   def __init__ (self, animal, animal_age):
     self.animal_type = animal
     self.age = int(animal_age)

   def change_type(self,str_in):
     self.animal_type = str_in

   def change_age(self,int_in):
      self.age = int(int_in)
   
   def get_type(self):
     print(self.animal_type)
    
lion = animal("lion", 10)
lion.get_type()