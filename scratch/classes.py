class Car:
	running = False
	no_of_wheels = 4
	
	def is_started(self):
		if self.running:
			print('The car is running')
		else:
			print('The car is not started')
			
print(f'This is from Car.running, value: {Car.running}')

my_car = Car()
my_car.running = True  # this references self.running
my_car.is_started()

print(f'This is from my_car.running {my_car.running}')

myData = 12355
print(myData)