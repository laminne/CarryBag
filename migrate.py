import sqlite3
dbname = 'meigen.db'

conn=sqlite3.connect(dbname)
c = conn.cursor()

create_table = 'create table meigen (id INTEGER PRIMARY KEY AUTOINCREMENT,body text)'
c.execute(create_table)