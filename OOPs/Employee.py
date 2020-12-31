class Employee:

    no_of_emps = 0
    raise_amount = 1.04 # class level variable

    def __init__(self,first,last,pay,company):
        self.first = first
        self.last = last
        self.email = first.lower() + '.' + last.lower() + '@'+ company.lower() +'.com'
        self.pay = pay

        Employee.no_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


##----------------------------------------------------------------------------------------------------##
#Creating instance of class
emp_1 = Employee('Thirunavukkarasu','A',100000,'jda')
emp_2 = Employee('Roshan','Kumar',98765400,'socgen')

print(emp_1) # Prints emp_1 instance address
print(emp_2) # Prints emp_2 instance address

print(emp_1.email) # Prints email adress of emp_1 instance
print(emp_2.email) # Prints email adress of emp_2 instance

# Print the fullname using class name
emp_3 = Employee('Shweta','Muchlambarkar',300000,'MetricStream')

print(Employee.fullname(emp_3))
#print(emp_3.email)
##----------------------------------------------------------------------------------------------------##
#Instance and Class variables
# Raise amount is a class level variable
print(Employee.raise_amount) # Class level variable
print(emp_3.pay)
Employee.apply_raise(emp_3)
print(emp_3.pay)
print ('-------------------------------')
emp_3.raise_amount = 1.8 # Instance level the class variable has been over written which impacts at the instance level
print(emp_3.raise_amount)
emp_3.pay = 300000

print(emp_3.pay)
Employee.apply_raise(emp_3)
print(emp_3.pay)

print(Employee.raise_amount) # Still the above class level variable is intact due to instance level change.

print('Total number of employees {}'.format(Employee.no_of_emps))




