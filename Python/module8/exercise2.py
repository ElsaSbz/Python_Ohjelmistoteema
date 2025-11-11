# Write a program that asks the user to enter the area code (for example FI) and prints out the airports located in that country ordered by airport type.
# For example, Finland has 65 small airports, 15 helicopter airports and so on.

import mysql.connector
def located_airport(area_code):
    sql = f"SELECT type , COUNT(*) FROM airport WHERE iso_country = '{area_code}' group by type ORDER BY type ASC"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
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
area = input("Enter area code: ")
located_airport(area)
