# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 13:53:44 2017

@author: richard
"""
"""
# create 
f = open('stocks.csv', 'r')
# read in file
data = f.read()
f.close()
"""

f = open('stocks.csv', 'r')
for line in f:
    print(line)
f.close


# Better way to read in a file, automatically closes file
with open('stocks.csv', 'r') as f:
    data = f.read()
#get rid of whitespace
line = line.strip()
#replace characters in the string
line.replace('"','-')

parts = line.split(',')
parts[0] = parts[0].strip('"')
parts[1] = parts[1].strip('"')
parts[2] = int(parts[2])
parts[3] = float(parts[3])

