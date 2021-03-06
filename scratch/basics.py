from typing import List

import numpy


def main():
    print("hello world")


if __name__ == "__main__":
    main()

myLst: List[int] = [1, 2, 3, 5, 7, 9]

print(myLst)

for counter in myLst:
    print(counter)

# create a list
mylist = ["richie", 1.84, "inge", 1.65, "alex", 1.67]
# change one item from a list
mylist[5] = 1.68
# change multiple items
mylist[0:2] = ["richard", 1.86]
# remove item from list
del(mylist[2])
# add item to list
mylist + ["kasper", 0.71]
# create new list and add item
mylist_ext = mylist + ["castor", 1.44, "pollux", 1.54]

# create a set
primesS = set((1, 2, 3, 5, 7))
# create a tuple
primesT = (1, 2, 3, 5, 7)
# create a list
primesL = [1, 2, 3, 5, 7]

# Test if item is in list
r = range(1, 5)
# test if value in range
1 in r

# Web Scraping
main_url = "https://www.humblebundle.com/"

import requests
result = requests.get(main_url)

result.text[:1000]


from bs4 import BeautifulSoup
soup = BeautifulSoup(result.text, 'html.parser')

print(soup.prettify()[:1000])

# Collections ##############
import collections as col

abc = 'jiwamotqgcfnudclzbyxkzmrvp'
mycount = col.Counter(abc)
print(2 in mycount.values())

# show type 
mycount.elements()
# show elements of collection
list(mycount.elements())
# show number of elements
len(list(mycount.elements()))


############ Python OOP #######################
############ Create a class  ###########
'''
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 40000)

# to print full name we can do:
print('{} {}'.format(emp_1.first,emp_1.last))

# or we create a method:
'''


class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1


    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 40000)
print(emp_1.fullname())
print(emp_2.email)
print(Employee.fullname(emp_1))

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_1.__dict__)
print(Employee.__dict__)

print(Employee.num_of_emps)




