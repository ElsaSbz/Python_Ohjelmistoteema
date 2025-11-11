# Write a program that asks the user to enter the cabin class of a cruise ship and then prints out a written description according to the list below.
# You must use an if/elif/else structure in your solution.

# LUX: upper-deck cabin with a balcony.
# A: above the car deck, equipped with a window.
# B: windowless cabin above the car deck.
# C: windowless cabin below the car deck.
# If the user enters an invalid cabin class, the program outputs an error message Invalid cabin class.

cabin_class=input("Enter the cabin class:")
if cabin_class == "LUX":
    print("The LUX cabin class is upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print ("The A cabin class is above the car deck, equipped with a window.")
elif cabin_class == "B" :
    print ("The B cabin class is windowless cabin above the car deck.")
elif cabin_class == "C":
    print ("The C cabin class is windowless cabin below the car deck.")
else :
    print ("The cabin class you entered is invalid")
