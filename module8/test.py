import mysql.connector

connection = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='test',
         user='elsa',
         password='123',
         autocommit=True
         )
