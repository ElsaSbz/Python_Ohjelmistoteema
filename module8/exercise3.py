#Write a program that asks the user to enter the ICAO codes of two airports.
# The program prints out the distance between the two airports in kilometers.
# The calculation is based on the airport coordinates fetched from the database.
# Calculate the distance using the geopy library: https://geopy.readthedocs.io/en/stable/.
# Install the library by selecting View / Tool Windows / Python Packages in your PyCharm IDE, write geopy into the search field and finish the installation.

import mysql.connector
import geopy.distance
def airport(icao):
    sql = (f"SELECT latitude_deg , longitude_deg  FROM airport WHERE ident = '{icao}';")
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result[0]

connection = mysql.connector.connect(
        host='localhost',
        port=3306,
        database='flight_game',
        user='elsa',
        password='123',
        autocommit=True
    )

icao1 = airport(input("Enter the first ICAO code: "))
icao2 = airport(input("Enter the second ICAO code: "))

distance = geopy.distance.distance(icao1, icao2).km
print(distance)