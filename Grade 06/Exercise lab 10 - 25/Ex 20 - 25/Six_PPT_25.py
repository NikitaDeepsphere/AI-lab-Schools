"""
Ex 25.

Finally, Add all the values to make 1 long string with each number seperated by a space

Program description: The objective of this program is to add all the values of a list containing different strings and make a large string.
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

for vAR_x in range(len(int_list)):
  int_list[vAR_x] = str(int_list[vAR_x])

print_me = ""
for vAR_x in range(len(int_list)):
  print_me = print_me + " " + int_list[vAR_x]
print(print_me)
