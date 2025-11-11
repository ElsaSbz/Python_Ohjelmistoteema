# Write a program that draws two random combinations of numbers for a combination lock:
# a 3-digit code where each number is between 0 and 9.
# a 4-digit code where each number is between 1 and 6.

import random


# Generate a 3-digit code (0-9)
x=str(random.randint(0,9))
y=str(random.randint(0,9))
z=str(random.randint(0,9))
print("3-Digit Code:", x+y+z )

# Generate a 3-digit code (1-6)
a=str(random.randint(1,6))
b=str(random.randint(1,6))
c=str(random.randint(1,6))
d=str(random.randint(1,6))
print("4-Digit Code:", a+b+c+d )


