# Write a program that asks the user how many dice to roll.
# The program rolls all the dice once and prints out the sum of the numbers. Use a for loop.
import random
dice=[]
sum = 0
dice_count=int(input("how many dice you want to roll ? "))
for i in range(dice_count):
    num = random.randint(1,6)
    dice.append(num)
    sum += dice[i]

print(f".{sum} is the sum of {dice} rolled dices.")