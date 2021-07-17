"""
Ex 5.

Given that each month has 30 days, and the date 7/7/2021 is a Wensday, create the function next, which will increase the day by one.
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