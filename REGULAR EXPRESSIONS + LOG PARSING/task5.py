<<<<<<< HEAD
# Task 5 (Final Challenge): Count how many times each IP failed login
#  Question:
# Create a dictionary where each IP address is a key and its value is the number of failed 
# attempts
import re
ip_regex = r"\d{1,3}(?:\.\d{1,3}){3}"
count = {}
with open("secure_log.txt", "r") as file:
    for line in file:
        if "Failed password" in line:
            ip_match = re.search(ip_regex, line)
            if ip_match:
                ip = ip_match.group()
            if ip in count:
                count[ip] += 1
            else:
                count[ip] = 1

                for ip, attempts in count.items():
                    print(f"{ip}:{attempts}")



=======
<<<<<<< HEAD
# Task 5 (Final Challenge): Write all "baduser" logins to a separate file
#  Question:
# Create a new file named badusers.txt and write all lines where the username starts with 
# "baduser".
#  Hint:
# • Use line.startswith("baduser")
# • Open new file in 'w' mode

with open("sample_logs.txt", "r") as infile:
    for line in infile:
        if line.startswith("baduser"):
            with open("Baduser.txt", "a") as outfile:
                outfile.write(line)
             
       
               
=======
# Task 5: Track Login Count Per User (Dictionary)
#  Question:
# From a list of logins, count how many times each user logged in and display the results.
#  Hint:
# • Use a dictionary: login_count = {}
# # • Loop through the list, use if user in dict

login_count = {}
list_of_logins = ["RT", "Dan", "Pan", "Human",]

for user in list_of_logins:
  if user in login_count:
    
    login_count[user] += 1
  else:
    login_count[user] = 1
print(login_count)
>>>>>>> f60046a0ca7766a20af443df501e4cb839e941c3
>>>>>>> 54e6b90c694ffb57d1c61e3c891a555c01f517a8
