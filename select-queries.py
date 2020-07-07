import sqlite3

conn = sqlite3.connect('helpdeskdb.db')
c = conn.cursor()

c.execute('SELECT * FROM activity')
print(c.fetchall())
