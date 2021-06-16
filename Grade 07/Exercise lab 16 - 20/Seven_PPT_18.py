"""
Ex 18.

Create a function that will take in a list of random numbers. Output those numbers, but sortest from least to greatest.
"""

check = [6,5,3,7,9,2,8,1,4,10]
def sort(check):
  out_list = check
  for x in range(len(out_list)):
    for x in range(len(out_list)-1):
      if(out_list[x] > out_list[x+1]):
        temp = out_list[x]
        out_list[x] = out_list[x+1]
        out_list[x+1] = temp
  return out_list

print(sort(check))