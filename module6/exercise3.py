# Write a function that gets the quantity of gasoline in American gallons and returns the number converted to litres.
# Write a main program that asks for a volume in gallons from the user and converts the value to liters. The conversion must be done by using the function. Conversions continue until the user inputs a negative value.
def conversion (g):
    return g * 3.78541
result = 0
while result >= 0:
    gallon = int(input("Enter volume of gasoline in gallon: "))
    result = conversion(gallon)
    if result < 0:
        print("Sorry, the volume cannot be negative")
        break
    print("the volume in litres is:", result)

