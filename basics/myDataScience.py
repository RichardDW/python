# ------------------ Python DataScience Tips and Tricks -------------

# Numpy ###
#### import a package
import numpy as np
#### to use a subset of the package:
# from numpay import array

fam = ['lisa',1.74,'emma',1.68,'mom',1.71,'dad',1.86]
print(fam + ['me',1.84])
print(fam)
# create a seperate (in memory) list, not a reference
y = list(fam)  # y = fam[:]
del y[2]
print(fam,y)
print(fam.reverse())

height = [1.73, 1.68, 1.71, 1.89, 1.79]
weight = [65.4, 59.2, 63.6, 88.4, 68.7]

# calculate BMI  -- weight / height ** 2
a = weight[0] / (height[0] * height[0])
print(a)

np_height = np.array(height)
np_weight = np.array(weight)

bmi = np_weight / np_height ** 2
print(bmi)

b = height + height
nb = np_height + np_height
print(b)
print(nb)


#######
from matplotlib import pyplot

data = open("life_expectancies_usa.txt", "r").readlines()

dates = []
male_life_expectancies = []
female_life_expectancies = []

for line in data:
    date, male_life_expectancy, female_life_expectancy = line.split(",")
    dates.append(date)
    male_life_expectancies.append(male_life_expectancy)
    female_life_expectancies.append(female_life_expectancy)
    
pyplot.plot(dates, male_life_expectancies, "bo-", label="Men")
pyplot.plot(dates, female_life_expectancies, "mo-", label="Female")
pyplot.legend(loc="upper left")
pyplot.ylabel("Age")
pyplot.xlabel("Year")
pyplot.plot("Life expectancies for women and in in the USA over time")

pyplot.show() 

###
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

