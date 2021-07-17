"""
Ex 7.

Create the function print date, which will print the date in the format day(from list), month/day/year. ie. Wensday, 7/7/2021
"""

days = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wensday", "Thursday"]
year = 2021
month = 1
day = 23

def next():
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

def print_date():
  return find_day(day,month,year) + ", " + str(month) + "/" + str(day) + "/" + str(year)

print(print_date())