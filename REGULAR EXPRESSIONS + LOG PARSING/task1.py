<<<<<<< HEAD
# Task 1: Extract all failed login attempts
#  Question:
# Write a program that prints all lines containing “Failed password”.
#  Hint:
# • Use re.search(r"Failed password", line)

import re
with open("secure_log.txt", "r") as file:
    for line in file:
        
            x = re.search(r"failed password", line)
            if "Failed password" in line:
                   print(line)
=======
<<<<<<< HEAD
# Task 1: Read the contents of a file
#  Question:
# Write a program to read all lines from sample_logs.txt and display them.
#  Hint:
# • Use open(filename, 'r') as f
# # • Use f.readlines() or loop over f

with open("sample_logs.txt", "r") as file:
 lines = file.readlines()
 for line in lines:
  print(line.strip())
=======
# Task 1: Welcome Users (Variables + Input + Print)
#  Question:
# Write a script that asks the user for their name and prints a welcome message.
#  Hint:
# • Use input() to ask the user’s name
# • Store it in a variable
# • Use print() to show a message


name = input("Enter your name:")
print(f"Welcome {name} in python codingS. I hope you are doing great in your life.")
>>>>>>> f60046a0ca7766a20af443df501e4cb839e941c3
>>>>>>> 54e6b90c694ffb57d1c61e3c891a555c01f517a8
