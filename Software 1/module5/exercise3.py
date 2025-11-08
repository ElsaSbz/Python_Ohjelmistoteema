# Write a program that asks the user for an integer and tells if the number is a prime number.
# Prime numbers are number that are only divisible by one or the number itself.
# For example, 13 is a prime number as it can only be divided by 1 or 13 so that the result is an integer.
# On the other hand, 21 is not a prime number as it is divisible by 3 and 7.
number = int(input("Enter an integer number: "))
dev_number = []
for i in range(2 ,number-1):
    if number % i == 0:
        dev_number.append (i)
if len(dev_number) > 0:
    print("The number is not prime and divisible by " , dev_number)
else :
    print("The number is  prime" )
