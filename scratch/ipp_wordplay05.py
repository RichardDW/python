# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 21:27:35 2018

@author: richard
"""

import time

my_words = [elt.strip() for elt in open("sonnet_words.txt", "r").readlines()]
word_list = [elt.strip() for elt in open("sowpods.txt", "r").readlines()]
word_dict = dict((elt,1) for elt in word_list)
word_set = set(word_list)

counter = 0

start = time.process_time()

for word in my_words:
#    if word not in word_list:
#    if word not in word_dict:
    if word not in word_set:
        print(word)
        counter += 1

stop = time.process_time()

print(f"Total new words: {counter} ")
print("Time elapsed: %.1f seconds" % (stop - start))