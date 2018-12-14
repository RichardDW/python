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