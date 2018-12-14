# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 19:28:25 2018

@author: richard
"""

import sqlite3

connection = sqlite3.connect("d://sqlite//jeopardy.db")
cursor = connection.cursor()

# Select a random category
cursor.execute("SELECT id, name FROM category ORDER BY RANDOM() LIMIT 1")
results = cursor.fetchall()

category_id, name = results[0]
print(name)

# Get and the clues for our random category
query = """SELECT text, answer, value FROM clue
WHERE category=%s ORDER BY value""" % (category_id,)
cursor.execute(query)
results = cursor.fetchall()

for clue in results:
    text, answer, value = clue
    print("[$%s]" % (value,))
    print("Question: %s" % (text,))
    print("Answer: What is '%s'?" % (answer))
    print("")

connection.close()


