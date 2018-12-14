#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 13:33:22 2017

@author: richard


next_line = "This is a test for encoding eand decoding strings to bytes and vv"
print(next_line.encode("utf-8"))
next_bytes = b'\xe6\x96\x87\xe8\xa8\x80'
print(next_bytes.decode("utf-8"))
"""
import random

print(random.randint(1,6))

def gen_squares(max_root):
    for n in range(max_root):
        yield n**2

squares=gen_squares(5)
type(squares)


