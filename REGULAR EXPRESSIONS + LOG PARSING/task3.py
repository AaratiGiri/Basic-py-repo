<<<<<<< HEAD
# Task 3: Extract IP addresses from all log lines
#  Question:
# Extract and print all IP addresses mentioned in the file.
#  Hint:
# • IP regex: \d{1,3}(?:.\d{1,3}){3}

import re

with open("secure_log.txt", "r") as file:
    for line in file:
        ip_regex = r"\d{1,3}(?:.\d{1,3}){3}"
        matches = re.findall(ip_regex, line)
        for ip in matches:
      
            print(ip)
=======
<<<<<<< HEAD
# Task 3: Extract username and time separately
#  Question:
# For each line, print just the username and timestamp.
#  Hint:
# • Use line.split() to split the line into words.

with open("sample_logs.txt", "r") as file:
 for line in file:
  parts = line.split()
  if len(parts) >= 1:
 
   print("username:", parts[0], "timestamp:", parts[1], parts[2])

 print(type(parts))
 print(type(line))


=======
# Task 3: Count Total Login Attempts (Loop + Counter)
#  Question:
# You have a list of usernames that tried to log in. Count how many total attempts there were.
#  Hint:
# • Use a for loop
# • Use a counter variable

usernames = ["Aarati", "Bob", "Nob", "sob", "aahan", "simon"]
count = 0
for user in usernames:
 count += 1
print( "The total attemots there were", count)
>>>>>>> f60046a0ca7766a20af443df501e4cb839e941c3
>>>>>>> 54e6b90c694ffb57d1c61e3c891a555c01f517a8
