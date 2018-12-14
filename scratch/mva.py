print('The capybara is the worlds largest rodent')
print('The capybara lives in groups')
print("The capybara can swim")

## get input from user
name = input('What is your name?')
print('Hello there ', name)
print (name.upper() )
print (name.lower() )
print (name.swapcase() )

country = input ('Where are you from? ')
country = country.upper()
print (country)

area = 0
length = 10
width = 20

area = width * length / 2
print('the area of the triangle will be %.2f' %area)


print('I have %d cats' % 6)
print('I have %7d cats' % 6)
print('I have %07d cats' % 6)
print('I have %7f cats' % 6)
print('I have %.2f cats' % 6)

print('I have {0:d} cats'.format(6))
print('I have {0:7d} cats'.format(6))
print('I have {0:07d} cats'.format(6))
print('I have {0:f} cats'.format(6))
print('I have {0:.2f} cats'.format(6))

print('Here are three numbers!' + \
    'The first is {0:d}, the second is {1:3d} and the third is {2:03d}'  .format(7,8,9)) 


import datetime
#print (datetime.date.today())
#print (datetime.time.dst(1) )

currDate = datetime.date.today()   
print (currDate)
print (currDate.year)
print (currDate.month)
print (currDate.day)


# http://strftime.org/
print (currDate.strftime('%d %b, %Y'))

#meanwhile earlier in the day
bestTeam = "senators"

#if statements with strings
#favouriteTeam = input("What is your favourite hockey team? ")
#if favouriteTeam.upper() == bestTeam.upper() :
#    print("Yeah Go Sens Go")
#    print("But I miss Alfredsson")
#print ("It's okay if you prefer football/soccer")

#if with numbers
freeToaster = None 

deposit = int(input("how much do you want to deposit "))
if deposit > 100 :
    freeToaster = True

#complex code here...
if freeToaster :
    print("enjoy your toaster")
print("Have a nice day!")

import turtle
#turtle.forward(100)
#turtle.right(90)
#turtle.colormode('green')
#turtle.left(40)

#for steps in range(4):
#    turtle.forward(100)
#    turtle.right(90)
#    for moresteps in range(4):
#        turtle.color('red')
#        turtle.forward(200)

nbrSides = 6
for steps in range(nbrSides):
    turtle.forward(100)
    turtle.right(360/nbrSides)
    for moresteps in range(nbrSides):
        #turtle.color('red')
        turtle.forward(50)
        turtle.right(360/nbrSides)
		


