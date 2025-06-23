class Employee:
    language = "Py" # this is a class attribute.
    salary = 120000

    def __init__(self, name, salary, language):   #Dunder Method: which is automatically called.
        self.name = name
        self.salary = salary
        self.language = language

        print("I'm creating an object.")

    def getInfo(self): # Self Parameter
        print(f"The language is {self.language}. The salary is {self.salary}")
    
    @staticmethod
    def greet(self):
        print("Good Morning")

harry = Employee("Harry", 1300000, "javascript")
# harry.name = "Harry"
print(harry.name, harry.salary, harry.language)

