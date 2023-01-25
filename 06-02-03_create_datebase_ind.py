import sqlite3
from sqlite3 import Error

conn = sqlite3.connect("database-hin.db")

c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS people(name TEXT, age INT, height REAL)')

c.execute('INSERT INTO people VALUES("Michele",25,5.10)')

conn.commit()
c.close
conn.close()

