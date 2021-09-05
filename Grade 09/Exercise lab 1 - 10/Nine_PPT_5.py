"""
Ex 5.

Program description: The objective of this program is given that each month has 30 days and the random date 7/7/2021 is Wednesday here this code to create a function named “next” which will increase the day by one.
"""

days = ["Sunday", "Monday", "Tuesday", "Wensday", "Thursday", "Friday", "Saturday"]
year = 2021
month = 7
day = 7

def next():
  if(day<31):
    day+=1
  else:
    day = 0
    month+=1
  if(month == 12):
    month = 1
    year+=1
