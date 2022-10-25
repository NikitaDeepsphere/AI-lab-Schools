"""
Ex 24.

Convert each number in the list from a int to a string
Program description: The objective of this program is to change the data type of the items in the list from integer to strings.

"""

vARint_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for vAR_x in range(len(vARint_list)):
  vARint_list[vAR_x]*=12

vAR_add = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
for vAR_x in range(len(vARint_list)):
  vARint_list[vAR_x] = (vARint_list[vAR_x] + vAR_add[vAR_x])

vAR_total = 0
for vAR_x in range (len(vARint_list)):
  vAR_total+= vARint_list[vAR_x]

for vAR_x in range(len(vARint_list)):
  vARint_list[vAR_x] = str(vARint_list[vAR_x])
