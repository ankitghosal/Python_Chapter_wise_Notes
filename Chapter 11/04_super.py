class Employee:
    def __init__(self):
        print("Construction of Employee")
    a = 1

class Programmer(Employee):
    def __init__(self):
        print("Construction of Programmer")
    b = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__()      #Addes super/ parent class as well ( like the mentioned class)
        print("Construction of Manager")
    c = 3


o = Employee()
print(o.a)

o = Programmer()
print(o.a, o.b)

o = Manager()
print(o.a, o.b, o.c)




