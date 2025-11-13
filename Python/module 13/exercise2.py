#Implement a backend service that gets the ICAO code of an airport and then returns the name and location of the airport in JSON format. The information is fetched from the airport database used on this course. For example, the GET request for EFHK would be: http://127.0.0.1:5000/airport/EFHK. The response must be in the format of: {"ICAO":"EFHK", "Name":"Helsinki-Vantaa Airport", "Location":"Helsinki"}.

import json
import mysql.connector
from flask import Flask, Response, render_template, request
app = Flask(__name__)
app.json.sort_keys = False
#app.config.from_object('config')
connection = mysql.connector.connect(
        host='localhost',
        port=3306,
        database='flight_game',
        user='elsa',
        password='123',
        autocommit=True
    )
@app.route("/airport/<icao>")


def airport(icao):
    sql = f"SELECT name, municipality FROM airport WHERE ident = '{icao}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        name, town = result
        response ={
            "icao": icao,
            "name": name,
            "location": town
        }
        return response
    else:
        response = json.dumps({"icao": icao, "name": "", "location": ""})
        return response(response=response,status=404,mimetypes="application/json")
    cursor.close()
    return

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
