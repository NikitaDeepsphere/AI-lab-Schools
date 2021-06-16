"""
Ex 30.

Create a System that will check whether or not a user's credentials match the correct username and password. Using user input, if the User's username matches "Billy" and the Users password matches "Clark123", then print("Access Granted"). Otherwise, print("Access Denied").
"""

username = input("Enter username:")
password = input("Enter password:")

print() #This is just so there is a space
if(username == "Billy" and password == "Clark123"):
  print("Access Granted")
else:
  print("Access Denied")