# Write a program that asks the user to enter numbers until they input an empty string to quit.
# At the end, the program prints out the five greatest numbers sorted in descending order.
# Hint: You can reverse the order of sorted list items by using the sort method with the reverse=True argument.
numbers = []
num = input("Enter the first number or quit by pressing Enter: ")
count = 0
while num!="":
    numbers.append(int(num))
    num = input("Enter the next number or quit by pressing Enter: ")
    count +=1

numbers.sort()
print(numbers)
print (count)
a = -1
for i in (0,count) :
    print(numbers[a])
    a = a - 1
    i = i + 1
