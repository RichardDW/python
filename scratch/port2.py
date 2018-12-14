# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 15:36:53 2017

@author: richard
"""

import csv

def portfolio_cost(filename, errors='warn'):
    '''
    Computes total shares * price for a CSV file with name, date, shares, price data
    '''
    if errors not in { 'warn', 'silent', 'raise' }:
        raise ValueError("errors must be one of 'warn', 'silent' or 'raise'")
        
    total = 0.0
    #f = open('stocks.csv', 'r')#f = open('stocks.csv', 'r') # old method
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)   # Skip a single line of input
        for rowno, row in enumerate(rows, start=1): # create a counter, rowno
            try:
                row[2] = int(row[2])
                row[3] = float(row[3])
            except ValueError as err:   # store error in err
                if errors == 'warn':
                    print('Row', rowno, 'Bad row', row)
                    print('Row', rowno, 'Reason:', err)
                elif errors == 'raise':
                    raise   # Reraise the last exception
                else:
                    pass    # ignore
                continue    # Skips to the next row
            total += row[2] * row[3]
    return total


import glob

files = glob.glob('stocks*.csv')
for filename in files:
    print(filename, portfolio_cost(filename, errors='raise'))

