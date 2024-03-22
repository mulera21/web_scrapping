import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

cursor.execute("SELECT* FROM events")
rows = cursor.fetchall()
print(rows)




