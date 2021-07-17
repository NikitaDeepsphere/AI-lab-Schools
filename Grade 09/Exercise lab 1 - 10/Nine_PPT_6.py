"""
Ex 6.

Create the function find day, which will find which day it is given the year, month, and day. Use the starting point, 1/1/2021, which is a Friday. Assume 360 days each year with each month having 30 days.
"""

days = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wensday", "Thursday"]
year = 2021
month = 7
day = 7

def next(self):
  if(day<31):
    day+=1
  else:
    day = 0
    month+=1
  if(month == 12):
    month = 1
    year+=1
  
def find_day(day, month, year):
  total = (day-1) + (month-1)*30 + (360 * (year-2021))
  return days[total%7]