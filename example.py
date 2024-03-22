import sqlite3

# establish a connection and a cursor
connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# query data
cursor.execute("SELECT* FROM events")
rows = cursor.fetchall()
print(rows)

# query certain coloumns
cursor.execute("SELECT band, date FROM events WHERE date = '2088.10.15'")
rows = cursor.fetchall()
print(rows)

# insert new rows  data
new_rows = [('dogs', 'dog City', '2088.10.16'),
            ('cats', 'cats city', '2088.10.12')]

cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_rows)
connection.commit()




