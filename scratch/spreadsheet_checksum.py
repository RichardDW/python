#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 11:26:54 2017

@author: richard
"""

import csv

checksum = 0

with open('/home/richard/Documents/spreads.txt') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    my_sheet = []
    for row in reader:
        my_row = []
        for r in row:
            my_row.append(int(r))
        #print(my_row)
        max_value = max(my_row)
        min_value = min(my_row)
        checksum = checksum + (max_value - min_value)
        print(max_value,'  ', min_value, '  ',max_value-min_value,'  ',checksum)
        my_sheet.append(my_row)

print('total of checksum is: ', checksum)     
   #     my_nb = np.append(my_sheet,row)

