class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 3

o = Employee()

print(o.a) # prints the a attribute
#print(o.b) # Shows an error as there is no b attribute in Employee class.

o = Programmer()
print(o.a, o.b)  # o.b gives result as it is made on Programmer where Employee is included.

o = Manager()
print(o.a, o.b, o.c) # as Manager  has both Employee & Programmer in it.







