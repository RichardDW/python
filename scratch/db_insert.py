# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 11:58:44 2018

@author: rwo

"""
import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file, create db if not exists.
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None

def insert_data(sql,mydata):
    try:
        mycursor.execute(sql,mydata)
    except sqlite3.IntegrityError as e:
        print('sqlite error ', e.args[0])  # column name is not unique
    mydbconn.commit

# create connection to database
mydb = 'c:\\sqlite\\db\\us_states.db'
mydbconn = sqlite3.connect(mydb)
mycursor = mydbconn.cursor()

# File for reading
STATE_LIST = "c:\\Data\src\\database\\us-states.txt"

mysql = '''INSERT INTO State (abbr, name, capitol) VALUES (?, ?, ?)'''

# read one line at a time
for line in open(STATE_LIST).readlines():
    # strip newline 
    line = line.strip()
    line = line.replace(' - ',',')
    line = line.split(sep=',')
    #print(line[0])
    #print(line[1])
    #print(line[2])
    #mydata=[line[0],line[1],line[2]]
    # write to table c:\sqlite\db\us_states.db
    # first establish connecting to database
    print(mysql, line)
    try:
        mycursor.execute(mysql,line)
    except sqlite3.IntegrityError as e:
        print('sqlite error ', e.args[0])  # column name is not unique
    mydbconn.commit()
    
mydbconn.close()

    
    
    
    
