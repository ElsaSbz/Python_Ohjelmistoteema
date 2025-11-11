# Write a program that asks the user for a username and password.
# If either or both are incorrect, the program ask the user to enter the username and password again.
# This continues until the login information is correct or wrong credentials have been entered five times.
# If the information is correct, the program prints out Welcome.
# After five failed attempts the program prints out Access denied.
# The correct username is python and password rules.
correct_username =  "python"
correct_password = "rules"
count = 0
while  count < 5:
    username=(input("Enter username : "))
    password=(input("Enter password : "))
    if password != correct_password or username != correct_username:
        print("Try again")
    else :
        print("Welcome")
        break
    count += 1
    if count == 5 and (password != correct_password or username != correct_username):
        print("Access denied")