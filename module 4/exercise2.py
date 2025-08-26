# Write a program that converts inches to centimeters until the user inputs a negative value. Then the program ends.
centimeter = input("Enter the centimeter: ")
centimeter = float(centimeter)
while centimeter >= 0:
    print(centimeter*0.393)
    centimeter = float(input("Enter the centimeter: "))
