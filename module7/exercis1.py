# Write a program that asks the user for a number of a month and then prints out the corresponding season
# (spring, summer, autumn, winter). Save the seasons as strings into a tuple in your program. We can define each season to last three months, December being the first month of winter.
season = ("winter","winter","spring", "spring","spring","summer","summer","summer", "autumn", "autumn","autumn","winter")
month_number= int(input("Enter the month number (1-12): "))
if 1 <= month_number <= 12:
    print("Welcome to",season[month_number-1])
