# Write a function that returns a random dice roll between 1 and 6. The function should not have any parameters.
# Write a main program that rolls the dice until the result is 6.
# The main program should print out the result of each roll.
import random
def dice_roll():
  return random.randint(1,6)
result = 0
while result != 6:
    result = dice_roll()
    print(result)
