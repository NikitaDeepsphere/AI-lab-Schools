"""
Ex 22.

Add Each value in the list (From Ex 21) to the corresponding value from: add = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

Program description: The objective of this program is to add each value in the list “vARint_list” to the corresponding value [3, 6,9,12,15,18,21,24,27,30]
The program highlights the usage of add function in python.

"""

vAR_int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for vAR_x in range(len(vAR_int_list)):
  vAR_int_list[vAR_x]*=12
vAR_add = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
for vAR_x in range(len(vAR_int_list)):
  vAR_int_list[vAR_x] = (vAR_int_list[vAR_x] + vAR_add[vAR_x])
