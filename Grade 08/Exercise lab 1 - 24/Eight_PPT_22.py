"""
Ex 22.

Add to the bank_account class 2 functions, withdraw and despoit, which will take in a integer input and add/subtract the the balance the corresponding amount.
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