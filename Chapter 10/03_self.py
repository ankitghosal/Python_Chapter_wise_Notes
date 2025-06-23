class Employee:
    language = "Py" # this is a class attribute.
    salary = 120000

    def getInfo(self): # Self Parameter
        print(f"The language is {self.language}. The salary is {self.salary}")
    
    def greet(self):
        print("Good Morning")


harry = Employee()
# harry.language = "Java Script" # this is a instance attribute.

harry.getInfo()
harry.greet()
# Employee.getInfo(harry)




