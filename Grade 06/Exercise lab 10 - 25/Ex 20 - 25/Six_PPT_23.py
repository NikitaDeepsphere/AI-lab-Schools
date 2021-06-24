"""
Ex 23.

Add Up all the values from each cell in the int_list (From Ex 22)
Program description: The objective of this program is to add up all the value from each call in the int_list.

"""

int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for vAR_x in range(len(int_list)):
  int_list[vAR_x]*=12

vAR_add = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
for vAR_x in range(len(int_list)):
  int_list[vAR_x] = (int_list[vAR_x] + vAR_add[vAR_x])

vAR_total = 0
for vAR_x in range (len(int_list)):
  vAR_total+= int_list[vAR_x]
