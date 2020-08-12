#! /usr/bin/env python
import sqlite3
conn = sqlite3.connect('/mnt/c/Users/mtatt/Documents/GitHub/CarryBag/meigen.db')
c = conn.cursor()

r = c.fetchall()
print("Content-Type: text/html\n")
c.execute('SELECT * FROM meigen')
for row in c.fetchall():
    b = row
    print(row)