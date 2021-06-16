"""
Ex 39.

Using the code for the last excersise, create another animal "Sally" whose age is 15 and gender is "Female"
"""

class animal:
   animal_name = ""
   age = 0
   gender = ""

   def __init__ (self, animal_name, animal_age, animal_gender):
     self.animal_name = animal_name
     self.age = int(animal_age)
     self.gender = animal_gender

   def change_name(self,str_in):
     self.animal_name = str_in

   def change_age(self,int_in):
      self.age = int(int_in)

   def change_gender(self,str_in):
      self.gender = str_in 
   
   def get_age(self):
     return self.age

   def get_name(self):
     return self.animal_name
   
   def get_gender(self):
     return self.gender


Fido = animal("Fido", 6, "Male")
print(Fido.get_name() , Fido.get_age())
Fido.change_name("Gumpy")

Sally = animal("Sally", 15, "Female")