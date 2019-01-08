def convert_to_celsius(fahrenheit):
	'''(number) -> number
	Return the degrees fahrenheit in celsius.

	>>>convert_to_celsius(32)
	0
	'''
	return fahrenheit -32 * 5 / 9

# Show class of an variable myvar
type(myvar)
# show object methods of a variable
dir(myvar)
# show the referenced (internal) id of a variable
id(myvar)

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

i = 524
result = 524
while i < 10508:
	i = i + 2
	result = result + i

print(result)



