# create a Class 'Employee' and add salary and increment properties to it.

# Write a method 'SalaryAttachment' method with a @property decorator with a setter which changes 
# the values of increment based on the salary.

class Employee:
    salary = 234
    increment = 20

    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))
    
# 2nd part
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary/self.salary) - 1)*100          # New Salary = Old Salary(1 + increment/100)


e = Employee()
print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 280.8
print(e.increment)




