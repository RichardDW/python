Python 3.2.3 (default, Sep 30 2012, 16:41:36) 
[GCC 4.7.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> def area(base,blah)
SyntaxError: invalid syntax
>>> def convert_to_celsius(fahrenheit):
	'''(number) -> number
	Return the degrees fahrenheit in celsius.

	>>>convert_to_celsius(32)
	0
	'''
	return fahrenheit -32 * 5 / 9

>>> convert_to_celsius(32)
14.222222222222221
>>> def convert_to_celsius(fahrenheit):
	'''(number) -> number
	Return the degrees fahrenheit in celsius.

	>>>convert_to_celsius(32)
	0
	'''
	return (fahrenheit - 32) * 5 / 9

>>> convert_to_celsius(32)convert_to_celsius(32)
SyntaxError: invalid syntax
>>> 
>>> convert_to_celsius(32)
0.0
>>> convert_to_celsius(212)
100.0
>>> convert_to_celsius(98)
36.666666666666664
>>> 


# Show class of an variable
type(<variable>)
# show object methods of a variable
dir(<variable>)
# show the referenced (internal) id of a variable
id(<variable>)

# tuple, t = (34,"t","tg",44,(55,66))

def minmax(items):
	return min(items), max(items)
	
minmax([83, 33, 44, 55, 12,555,32,4,99])

lower, upper = minmax([83, 33, 44, 55, 12,555,32,4,99])

lower
upper

#swap 2 variables
a1 = 45
a2 = 66
a1, a2 = a2, a1

myline = "Hello there from beyond"
myline.split()
mycsv = "number,of,words,on,a,line"
mycsv.split(',')
mycsv.split(',')[2]

# join on an empty seperator
''.join(['high','way','man'])


