# --- Python class and OO snippets -----------
'''
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 40000)

# to print full name we can do:
print('{} {}'.format(emp_1.first,emp_1.last))

# or we create a method:
'''


class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1


    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 40000)
print(emp_1.fullname())
print(emp_2.email)
print(Employee.fullname(emp_1))

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_1.__dict__)
print(Employee.__dict__)

print(Employee.num_of_emps)
