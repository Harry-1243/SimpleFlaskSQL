from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route('/create')
def create():
	con = sqlite3.connect('car.db')
	cur = con.cursor()
	cur.execute(	"""	CREATE TABLE Car(
					Model VARCHAR(20) NOT NULL PRIMARY KEY,
					HorsePower INTEGER NOT NULL)
			""")
	con.commit()
	return 'CREATE'

@app.route('/insert')
def insert():
	con = sqlite3.connect('car.db')
	cur = con.cursor()
	cur.execute(	"""	INSERT INTO Car (Model, HorsePower)
					VALUES ("Volvo XC90", "287")
			""")
	con.commit()
	return 'INSERT'

@app.route('/select')
def select():
	con = sqlite3.connect('car.db')
	cur = con.cursor()
	cur.execute("SELECT * FROM Car")
	rows = cur.fetchall()
	return str(rows)
