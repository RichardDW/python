# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 21:22:07 2018

@author: richard
"""

# LIST COMPREHANSION

my_list = ["a", "b" , "c", "d", "e"]
[elt for elt in my_list]

[elt*2 for elt in my_list]

squares = [elt * elt for elt in range(10)]

word_list = [elt.strip() for elt in open("sowpods.txt", "r").readlines()]

[elt for elt in word_list]

[elt for elt in word_list if "UU" in elt]

[word for word in word_list if word == word[::-1]]

cijfer = 60606

str(cijfer) == str(cijfer)[::-1]

woord = "appelflap"

from matplotlib import pyplot
pyplot.plot([0,2,4,6,8,10], "o")
pyplot.ylabel("Values")
pyplot.xlabel("Time")
pyplot.title("Test plot")
pyplot.show()

def gen_squares(max_root):
    for n in range(max_root):
        yield n**2

squares=gen_squares(5)
type(squares)

for square in squares: print(square)

squares2=gen_squares(6)
next(squares2)
next(squares2)

def gen_up_to(limit):
    n = 0
    while n <= limit:
        yield n
        n += 1

it = gen_up_to(10)

it.__next__()
next(it)

next(it, None)


def myitems(top):
    while top > 0:
        yield top**2
        top -= 1
    yield "All done"
    
for item in myitems(3):
    print(item)
    
