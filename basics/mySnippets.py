# Python tips and tricks

def main():
    print("hello world")

if __name__ == "__main__":
    main()

# -----

def main(url):
    get_something(url)


if __name__ == '__main__':
    main(sys.argv[1])


# ----------- System \ File functions --------------------------------------
import sys

if len(sys.argv) != 3:
        raise SystemExit('Usage:',  sys.argv[0], 'route, stopid')
# assign arguments to variables
route = sys.argv[1]
stopid = sys.argv[2]
#--
route, stopid = argv

# to terminate program 
raise SystemExit(0)

import os
if os.path.isdir("/tmp"):
    print ("/tmp is a directory")
else:
    print ("/tmp is not a directory")

# -----
from pathlib import Path

p = Path('.')
[x for x in p.iterdir() if x.is_dir()]

try:
    open(p)
except IOError:

# check to see whether p is a file
p.is_file()
# check to see whether p is a directory
p.is_dir()

# list specific files in a directory
import os,glob

os.chdir("/home/rwo/Download")
for file in glob.glob("*.gz"):
    print(file)



## open and read in file
sonnets = open("sonnets.txt").readlines()
word_set = set([elt.strip() for elt in open("sowpods.txt")])
sonnet_words = set()

my_words = [elt.strip() for elt in open("sonnet_words.txt", "r").readlines()]
word_list = [elt.strip() for elt in open("sowpods.txt", "r").readlines()]


## strip and clean input from file
for line in sonnets:
    # Split apart hyphenated words.
    line_words = line.replace("-", " ").strip().split()

    # It's an empty line or a sonnet number; skip it.
    if len(line_words) <= 1:
        continue

    for word in line_words:
        stripped = strip_punctuation(word)
        if stripped and len(stripped) > 1:
            sonnet_words.add(stripped.upper())
###
import os
# open file from ..\database\US_state_capitols.txt
# read a line
STATE_LIST = "c:\\Data\src\\database\\US_state_capitols.txt"
with open(STATE_LIST, 'r') as f:
    statecap = f.read()
statecap = statecap.strip('\n')
statecap = statecap.replace(",","\n")
statecap = statecap.strip()

parts = statecap.split(':')
#parts = statecap.replace(':','')

#----------------

statecap = open(STATE_LIST).readlines()
# Get rid of newlines and white space
statecap = [word.strip() for word in statecap]
for line in statecap:
    print(f'this is a line {line}')
    print('\n')

#----------------
for line in open(STATE_LIST).readlines():
    # strip newline
    line = line.strip()
    #line = line.strip("'")
    line = line.replace("'","",4)
    line = line.split(sep=',')

fo = open(STATE_LIST)
my_numbers = fo.read()
# one liner to open and read file as list
my_numbers2 = open(STATE_LIST).readlines()

# check if last character is newline character
if my_numbers[-1] == '\n' :
    print('Newline found...stripping\n')
    my_numbers = my_numbers.rstrip('\n')
else:
    print('No newline found!\n')

# ---------- Variables -------------
# Show class of an variable myvar
type(myvar)
# show object methods of a variable
dir(myvar)
# show the referenced (internal) id of a variable
id(myvar)

#swap 2 variables
a1 = 45
a2 = 66
a1, a2 = a2, a1

# join on an empty seperator
''.join(['high','way','man'])

lower, upper = minmax([83, 33, 44, 55, 12,555,32,4,99])


# --------------- Lists, sets, dictonairies, arrays, etc ------------

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

# -----------------------
# The get() method on dicts
# and its "default" argument

name_for_userid = {
    382: "Alice",
    590: "Bob",
    951: "Dilbert",
}

def greeting(userid):
    '''
    >>> greeting(382)
    "Hi Alice!"

    >>> greeting(333333)
    "Hi there!"
    '''
    return "Hi %s!" % name_for_userid.get(userid, "there")

a = ['foo', 'bar', 'baz']
while a:
    print(a.pop(-1))


# ===================================
a = ['foo', 'bar', 'baz', 'qux']
s = 'corge'
i = 0
    while i < len(a):
        if a[i] == s:
            #Processing for item found
            break
        i += 1
    else:
        # Processing for item not found
        print(s, 'not found in list.')

#---OR ---

if s in a:
    print(s, 'found in list.')
else:
    print(s, 'not found in list.')

#---- OR ---

try:
    print(a.index('corge'))
except ValueError:
    print(s, 'not found in list.')


# LIST COMPREHENSION

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

# Create a single string from all elements in list
a = ["Python", "is", "awsome"]  # list
b = (" ".join(a))  # String

# find most frequent value in a list
a = [1,2,3,6,5,6,5,8,9,1,3,2,3,8,7,3,4,4,4,6,8,4,3,4,3,1]
print(max(set(a),key = a.count))

# ---------------- Collections ---------------------
# find most frequent value in a list
''' Using Counter from collections'''
from collections import Counter

cnt = Counter(a)
print(cnt.most_common(3))


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


# ---------------------- Itertools, iterations -------------
import itertools

counter = itertools.count()

# infinite loop
for num in counter:
    print(num)

# each print will print next number
print(next(counter))

# the zip function pairs data
data = [100, 200, 300, 400]
daily_data = zip(itertools.count(), data)
# or convert to a list right away
daily_data = list(zip(itertools.count(), data))


def squared(x):
    return x * x


for i in range(10):
    print("{} squared is {}".format(i, squared(i)))
    print(f"{i} squared is {squared}.")

n = int(input())
for i in range(0,n):
    print(i*i)


# ----------------- Encoding ----------------------	
next_line = "This is a test for encoding eand decoding strings to bytes and vv"
print(next_line.encode("utf-8"))
next_bytes = b'\xe6\x96\x87\xe8\xa8\x80'
print(next_bytes.decode("utf-8"))	


# ------------- Decorators --------------------------------
def printlog(func):
    def wrapper(arg):
        print("CALLING: " + func.__name__)
        return func(arg)
    return wrapper
@printlog
def f(n):
    return n+2

print(f(3))


def money_format(func):
    def wrapper(*args, **kwargs):
        r = func(*args, **kwargs)
        formatted = '£{:.2f}'.format(r)
        return formatted
    return wrapper


@money_format
def add_tax(value, tax_percentage):
    return value * (1 + (tax_percentage / 100))

add_tax(101,21)



# -----------------
# Fibonacci sequence
a, b = 0, 1
for i in range(0, 10):
    print(a)
    a, b = b, a + b

# ----------------  Web scraping --------------------------

main_url = "https://www.humblebundle.com/"

import requests
result = requests.get(main_url)
result.text[:1000]
data = requests.get('https://www.omroep.nl')
data2 = requests.head('https://www.omroep.nl')

from bs4 import BeautifulSoup
soup = BeautifulSoup(result.text, 'html.parser')

print(soup.prettify()[:1000])

##########################################
import urllib.request as ur

# valid route = 22, valid stopid = 14787 / 14791
# valid route = 6, valid stopid = 5037
u = ur.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?route={}&stop={}'.format(route,stopid))
data = u.read()

from xml.etree.ElementTree import XML
doc = XML(data)

for pt in doc.findall('.//pt'):
    print(pt.text)

def fetch_words(url):
    """Fetch a list of words from an URL

    Args:
        url: The URL of a UTF-9 text document.
        example: http://sixty-north.com/c/t.txt

    Returns:
        A list of strings containing the words from
        the document.
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words




#------------- Time conversion -----------------


def convert_to_minutes(num_hours):
    '''(int) -> int
    Return the number of minutes there are in num_hours
    >>> convert_to_minutes(2)
    120
    '''
    minutes = num_hours * 60
    return minutes

def convert_to_seconds(num_hours):
    '''(int) -> int
    Return the number of seconds there are in num_hours
    >>> convert_to_seconds(2)
    7200
    '''
    minutes = convert_to_minutes(num_hours)
    seconds = minutes * 60
    return seconds

def seconds_difference(time_1, time_2):
    '''(float, float) -> float

    Return the number of seconds later that a time in seconds
    time_2 is than a time in seconds time_1.
        
    >>> seconds_difference(1800.0, 3600.0)
    1800.0
    >>> seconds_difference(3600.0, 1800.0)
    -1800.0
    >>> seconds_difference(1800.0, 2160.0)
    360.0
    >>> seconds_difference(1800.0, 1800.0)
    0.0
    '''
    return time_2 - time_1


def hours_difference(time_1, time_2):
    '''(float, float) -> float

    Return the number of hours later that a time in seconds
    time_2 is than a time in seconds time_1.
        
    >>> hours_difference(1800.0, 3600.0)
    0.5
    >>> hours_difference(3600.0, 1800.0)
    -0.5
    >>> hours_difference(1800.0, 2160.0)
    0.1
    >>> hours_difference(1800.0, 1800.0)
    0.0
    '''
    return (time_2 * 10 / 36000) - (time_1 * 10 / 36000)

def to_24_hour_clock(hours):
    '''(number) -> number

    hours is a number of hours since midnight. Return the
    hour as seen on a 24-hour clock.

    Precondition: hours >= 0

    >>> to_24_hour_clock(24)
    0
    >>> to_24_hour_clock(48)
    0
    >>> to_24_hour_clock(25)
    1
    >>> to_24_hour_clock(4)
    4
    >>> to_24_hour_clock(28.5)
    4.5
    '''
    return hours % 24




