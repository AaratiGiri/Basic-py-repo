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
