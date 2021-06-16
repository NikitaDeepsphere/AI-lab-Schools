"""
Ex 27.

Add to the preivous class and create a function change_type that changes the type of the animal based on what is passed in.

Hint: remember to use self as one of the parameters passed into the function
"""

class animal:
   animal_type = ""

   def change_type(self,str_in):
     self.animal_type = str_in