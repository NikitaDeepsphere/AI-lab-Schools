"""
Ex 46.

Create a class called bank_account that has the variables balance and id_number. The constructor will take in a number for the balance and the id_number will be a random 6-digit number.
"""

import random

class bank_account:
  balance = 0
  id_number = 0

  def __init__(self, num):
    self.balance = num
    self.id_number = random.randrange(100000,999999)