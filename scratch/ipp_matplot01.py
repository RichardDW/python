# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 12:44:29 2018

@author: richard
"""

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
