from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="database",
    user="root",
    password="password",
    database="mydb"
)

@app.route('/')
def get_users():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    return jsonify(results)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)