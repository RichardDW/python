# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 20:51:15 2018

@author: richard
"""

def printlog(func):
    def wrapper(arg):
        print("CALLING: " + func.__name__)
        return func(arg)
    return wrapper
@printlog
def f(n):
    return n+2

print(f(3))

import requests

data = requests.get('https://www.omroep.nl')
data2 = requests.head('https://www.omroep.nl')