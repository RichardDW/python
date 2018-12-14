# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 18:08:24 2018

@author: richard
"""

import sqlite3

connection = sqlite3.connect("jeopardy.db")
cursor = connection.cursor()

cursor.execute("SELECT text, answer, value FROM clue LIMIT 10")
results = cursor.fetchall()

# process results
for clue in results:
#    text = clue[0]
#    answer = clue[1]
#    value = clue[2]
    # via the of tuple unpacking
    text, answer, value = clue
    
    # [$200]
    # Question: kjkjdfdf
    # Answer: what is kjkjdfdf
    
    print("[$%s]" % (value))
    print("Question: %s" % (text,))
    print("Answer: What is '%s'?" % (answer))
    print("")
    

# close connection
connection.close()
