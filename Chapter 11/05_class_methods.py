class Employee:
    a = 1

    @classmethod    #sticks only to Class attribute. Don't show Instance attribute
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e = Employee()
e.a = 45

e.show()
