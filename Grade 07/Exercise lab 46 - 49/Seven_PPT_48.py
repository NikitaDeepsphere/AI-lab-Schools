"""
Ex 48.

Add to the bank_account class a function called verify, which will take in user input using input(), and check and see if the id_numbers match return a boolean corresponding to whether they match or not
"""

import random

class bank_account:
  balance = 0
  id_number = 0

  def __init__(self, num):
    self.balance = num
    self.id_number = random.randrange(100000,999999)

  def withdraw(self, num):
    self.balance = self.balance - num
    return self.balance
  
  def deposit(self, num):
    self.balance = self.balance + num
    return self.balance
  
  def verify(self):
    return self.id_number == int(input("What is your id_number?"))
  
  def get_id_num(self):
    return self.id_number