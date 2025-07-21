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