# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 15:34:26 2018

@author: richard
"""

import sqlite3

connection = sqlite3.connect("jeopardy.db")
#help(connection)
#dir(connection)
cursor = connection.cursor()
#dir(cursor)

cursor.execute("SELECT name FROM category LIMIT 10")
results = cursor.fetchall()

print("Example categories:\n")
for category in results:
    print(category[0])

connection.close()
