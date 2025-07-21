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
