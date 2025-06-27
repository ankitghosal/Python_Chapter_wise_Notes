class Employee:
    a = 1

    @classmethod    #sticks only to Class attribute. Don't show Instance attribute
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property
    def name(self):
        return f"{self.ename} {self.lname}"

    @name.setter
    def name (self,value):
        self.fname = value.split(" ")[0]  # fname = First Name - [0] = 1st element 0
        self.lname = value.split(" ")[1]  # lname = Last Name - [1] = 2nd element 1


e = Employee()
e.a = 45
e.name = "Harry Khan"
print(e.fname, e.lname)


e.show()
