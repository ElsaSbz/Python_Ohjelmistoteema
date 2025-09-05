# Write a function that receives two parameters: the diameter of a round pizza in centimeters and the price of the pizza in euros.
# The function calculates and returns the unit price of the pizza per square meter.
# The main program asks the user to enter the diameter and price of two pizzas and tells the user which pizza provides better value for money (which of them has a lower unit price).
# You must use the function you wrote for calculating the unit prices.

def pizza ( round , price) :
    round_m = round / 100
    return price / round_m
first_round = float(input("Enter the first pizza's round in centimeter: "))
first_price = float(input("Enter the first pizza's price in euro: "))
first_value = pizza ( round = first_round, price = first_price)
second_round = float(input("Enter the second pizza's round in centimeter: "))
second_price = float(input("Enter the second pizza's price in euro: "))
second_value = pizza ( round = second_round, price = second_price)
if first_value < second_value:
    print("The first pizza is better than the second pizza")
elif first_value > second_value:
    print("The second pizza is better than the first pizza")
else:
    print("Both pizza have the same value")
