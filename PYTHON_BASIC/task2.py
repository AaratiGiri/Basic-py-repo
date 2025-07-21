# Task 2: Block Unauthorized Users (Conditionals)
#  Question:
# Check if the entered username is in a list of blocked users. If yes, print “Access Denied”, else 
# “Access Granted”.
#  Hint:
# • Create a list: blocked = ["hacker", "intruder"]
# • Use an if...else condition


list = ["hacker", "intruder"]

username = input("Enter you name:")
if username in list:
  print("Access Denied.")
else:
  print("Access Granted")