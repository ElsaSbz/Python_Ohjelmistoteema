# Write a program that asks the user to enter numbers until they enter an empty string to quit.
# Finally, the program prints out the smallest and largest number from the numbers it received.
number = input("Enter the number: ")
min_number = float(number)
max_number = float( number)
while number != " ":
    if min_number >= float(number):
        min_number = float(number)
    if max_number <= float(number):
        max_number = float(number)
    number = input("Enter the number: ")
print(f".{min_number} is the minimum number")
print(f".{max_number} is the maximum number")




