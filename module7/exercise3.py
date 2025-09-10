# Write a program for fetching and storing airport data.
# The program asks the user if they want to enter a new airport, fetch the information of an existing airport or quit.
# If the user chooses to enter a new airport, the program asks the user to enter the ICAO code and name of the airport.
# If the user chooses to fetch airport information instead, the program asks for the ICAO code of the airport and prints out the corresponding name.
# If the user chooses to quit, the program execution ends.
# The user can choose a new option as many times they want until they choose to quit. (The ICAO code is an identifier that is unique to each airport. For example, the ICAO code of Helsinki-Vantaa Airport is EFHK. You can easily find the ICAO codes of different airports online.)

order =int(input("What would you like to do? "
             "1. enter a new airport,"
             " 2.fetch the information of an existing airport "
             "3.quit"))
airports ={"ICAO" : "airport_name" }
while order !=3:
    if order==1:
        icao=input("Enter the ICAO code: ")
        airport_name=input("Enter the airport name: ")
        airports[icao]=airport_name
        print (airports[icao])
    elif order==2:
        icao=input("Enter the ICAO code: ")
        print (airports[icao])
    elif order==3:
        print("Bye!")
        break
    order = int(input("What would you like to do? "
                      "1. enter a new airport,"
                      " 2.fetch the information of an existing airport "
                      "3.quit"))
print("Bye!")
