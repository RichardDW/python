#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 10:46:05 2017

@author: richard
"""

import csv

total = 0

with open('/home/richard/Documents/spreads.txt') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    my_sheet = []
    for row in reader:
        my_row = []
        for r in row:
            my_row.append(int(r))
        my_sheet.append(my_row)
        for number1 in my_row:
            for number2 in my_row:
                if number1 == number2:
                    pass
                elif number1 % number2 == 0:
                    total = total + (number1 / number2)

print('total will be: ', total)
                    
            