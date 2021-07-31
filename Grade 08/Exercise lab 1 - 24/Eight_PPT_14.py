"""
Ex 14.

The objective of this program is to create a function that will check whether the sum of a list that is imputed is equal to 21.
"""

check = [1,2,-3,3,3,4,5,6,2,-2]
def sum21(list):
  vAR_total = 0
  for vAR_x in check:
    vAR_total+=vAR_x
  if(vAR_total == 21):
    return True
  else:
    return False

print(sum21(check))
