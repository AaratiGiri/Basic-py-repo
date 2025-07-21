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
             
       
               