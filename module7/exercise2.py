# Write a program that asks the user to enter names until he/she enters an empty string.
# After each name is read the program either prints out New name or Existing name depending on whether the name was entered for the first time.
# Finally, the program lists out the input names one by one, one below another in any order.
# Use the set data structure to store the names.
names = set()
name=input("Enter your name: ")
while name != " ":
    if name in names:
        print("existed name")
    else :
        print("new name")
    names.add(name)
    name=input("Enter your name: ")
for name in names:
    print (name)
