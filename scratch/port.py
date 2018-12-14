# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 15:15:57 2017

@author: richard
"""

"""
#port.py
total = 0.0
#f = open('stocks.csv', 'r')#f = open('stocks.csv', 'r') # old method
with open('stocks.csv', 'r') as f:
    headers = next(f)   # Skip a single line of input
    for line in f:
        line = line.strip()   # strip whitespace
        parts = line.split(',')
        parts[0] = parts[0].strip('"')
        parts[1] = parts[1].strip('"')
        parts[2] = int(parts[2])
        parts[3] = float(parts[3])
        total += parts[2]*parts[3]
        
print('Total cost:', total)

"""
"""
import csv

with open('stocks.csv', 'r') as f:
    rows = csv.reader(f)
    for row in rows:
        print(row)
"""

#port2.py
# now using csv

import csv

total = 0.0
#f = open('stocks.csv', 'r')#f = open('stocks.csv', 'r') # old method
with open('stocks.csv', 'r') as f:
    rows = csv.reader(f)
    headers = next(rows)   # Skip a single line of input
    for row in rows:
        row[2] = int(row[2])
        row[3] = float(row[3])
        total += row[2] * row[3]
        
print('Total cost:', total)