
class Employee:
    pass

emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

emp_1.first='Jam'
emp_1.last='Green'
emp_1.email='JamGreen@12.com'
emp_1.pay=10000

print(emp_1.first)
print(emp_1.last)

print('{} {}'.format(emp_1.first,emp_1.last))