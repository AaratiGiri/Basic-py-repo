<<<<<<< HEAD
# Task 2: Extract all usernames from failed logins
#  Question:
# Print only usernames (like baduser1, baduser2) from lines with failed logins.
#  Hint:
# • Use a pattern like: r"Failed password for (\w+)"

import re
with open("secure_log.txt", "r") as file:
    for line in file:
        if re.search(r"baduser", line):
         print(line)
=======
<<<<<<< HEAD
# Task 2: Find all login attempts by baduser1
#  Question:
# From the log, print only the lines that contain "baduser1".
#  Hint:
# # • Use "if 'baduser1' in line:" inside a loop.

with open("sample_logs.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        if 'baduser1' in line:
            print(line)
            
=======
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
>>>>>>> f60046a0ca7766a20af443df501e4cb839e941c3
>>>>>>> 54e6b90c694ffb57d1c61e3c891a555c01f517a8
