import mysql.connector
from flask import Flask, request

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='samik',
    password='volvo240',
    autocommit=True,
    collation='utf8mb4_general_ci'
)
app = Flask(__name__)
@app.route('/ICAO/<icao>')
def ICAOGET(icao):
    sql = (f"select name, ident from airport where ident= %s")
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql, (icao,))
    result = cursor.fetchone()
    vastaus = {
        "ICAO": result['ident'],
        "Name": result['name'],
    }

    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)