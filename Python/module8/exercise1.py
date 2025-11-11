# Write a program that asks the user to enter the ICAO code of an airport. The program fetches and prints out the corresponding airport name and location (town) from the airport database used on this course. The ICAO codes are stored in the ident column of the airport table.

import mysql.connector
def airport(icao):
    sql = f"SELECT name, municipality FROM airport WHERE ident = '{icao}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        name, town = result
        print(f"Airport Name: {name}")
        print(f"Location: {town}")
    else:
        print("No airport found with that ICAO code.")
    cursor.close()
    return

connection = mysql.connector.connect(
        host='localhost',
        port=3306,
        database='flight_game',
        user='elsa',
        password='123',
        autocommit=True
    )

icao = input("Enter ICAO code: ")
airport(icao)
