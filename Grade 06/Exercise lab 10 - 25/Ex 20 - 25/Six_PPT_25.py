"""
Ex 25.

Finally, Add all the values to make 1 long string with each number seperated by a space
"""

int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for x in range(len(int_list)):
  int_list[x]*=12

add = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
for x in range(len(int_list)):
  int_list[x] = (int_list[x] + add[x])

total = 0
for x in range (len(int_list)):
  total+= int_list[x]

for x in range(len(int_list)):
  int_list[x] = str(int_list[x])

print_me = ""
for x in range(len(int_list)):
  print_me = print_me + " " + int_list[x]
print(print_me)