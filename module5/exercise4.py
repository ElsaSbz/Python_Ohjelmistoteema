# Write a program that asks the user to enter the names of five cities one by on (use a for loop for reading the names) and stores them into a list structure.
# Finally, the program prints out the names of the cities one by one, one city per line, in the same order they were read as input. Use a for loop for asking the names and a for/in loop to iterate through the list.
city = []
for i in range(1,6):
    city.append(input("Enter the city name: "))
for name in city:
    print(name)