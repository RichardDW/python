# multiply all digits of a number and repeat.
# search for a string that has the most steps to 
# repeat this process. It is called
# multiplicative persistence

def per(n):
	if len(str(n))==1:
		print(n)
		return "DONE"
		
	digits = [int(i) for i in str(n)]
	
	result = 1
	for j in digits:
		result *= j
	print(result)

	per(result)