"""
Ex 23.

Add Up all the values from each cell in the vARint_list (From Ex 22)
Program description: The objective of this program is to add up all the value from each call in the vARint_list.

"""


for vAR_x in range(len(vARint_list)):
  vARint_list[vAR_x]*=12

vAR_add = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
for vAR_x in range(len(vARint_list)):
  vARint_list[vAR_x] = (vARint_list[vAR_x] + vAR_add[vAR_x])

vAR_total = 0
for vAR_x in range (len(vARint_list)):
  vAR_total+= vARint_list[vAR_x]
