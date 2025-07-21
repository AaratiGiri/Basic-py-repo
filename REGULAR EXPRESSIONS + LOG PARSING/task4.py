<<<<<<< HEAD
# Task 4: Combine username and IP in a single output
#  Question:
# For each failed login, print username and IP like:
# baduser1 → 192.168.1.25
import re

ip_regex = r"\d{1,3}(?:\.\d{1,3}){3}"

with open("secure_log.txt", "r") as file:
    for line in file:
        if "Failed password" in line:
            user_match = re.search(r"Failed password for (\w+)", line)
            ip_match = re.search(ip_regex, line)
            if user_match and ip_match:
                username = user_match.group(1)
                ip = ip_match.group()
                print(f"{username} -> {ip}")


     
     




          
=======
<<<<<<< HEAD
# Task 4: Count login attempts per user
#  Question:
# Count how many times each user tried to log in.
#  Hint:
# • Use a dictionary and loop through usernames
login_count = {}
with open("sample_logs.txt", "r") as file:
    for line in file:
        parts = line.split()
        if len(parts) >= 3:
            user = parts[0]
            if user in login_count:
                login_count[user] += 1
            else:
                login_count[user] = 1

for user, count in login_count.items():
     print(f"{user} has tried {count} times")

            
               
    
    
        
=======
# Task 4: Find Unique Users (List + Set)
#  Question:
# From the same list, find how many unique users tried to log in.
#  Hint:
# • Convert the list to a set using set()
count = 0
usernmaes = ["Aarati", "Bob", "Nob", "sob", "aahan", "simon", "Aarati", "asli"]
unique_users = set(usernmaes)
for user in unique_users:
 count += 1
  
print(count)
print(unique_users)
>>>>>>> f60046a0ca7766a20af443df501e4cb839e941c3
>>>>>>> 54e6b90c694ffb57d1c61e3c891a555c01f517a8
