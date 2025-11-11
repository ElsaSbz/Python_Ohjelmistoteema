# Write a program that asks a fisher the length of a zander in centimeters.
# If the zander does not fulfill the size limit, the program instructs to release the fish back into the lake and notifies the user of how many centimeters below the size limit the caught fish was.
# A zander must be 42 centimeters or longer to meet the size limit.
zander_length=float(input("Enter the length of zander: "))
if zander_length < 42:
    print("Release the fish back to lake because the length of zander is" , 42 - zander_length, "less than size limit")
else:
    print ("the length of the fish is ok and you can keep it")