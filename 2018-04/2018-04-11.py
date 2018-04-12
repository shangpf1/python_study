
class Employee:
    

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.email = first+last+'@123.com'
        self.pay = pay

    
    def fullname(self):
        return('{} {}'.format(self.first,self.last))

emp_1 = Employee('hello','world',1900)
emp_2 = Employee('test','world',2000)

print(emp_1)
print(emp_2)

print(emp_1.fullname())
print(emp_2.fullname())
