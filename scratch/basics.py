import numpy

def main():
    print("hello world")


if __name__ == "__main__":
    main()




myLst = [1,2,3,5,7,9]

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

#create a set
primesS = set((1,2,3,5,7))
#create a tuple
primesT = (1,2,3,5,7)
#create a list
primesL = [1,2,3,5,7]