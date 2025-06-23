class Employee:
    language = "Py" # this is a class attribute.
    salary = 120000


harry = Employee()
harry.language = "Java Script" # this is a instance attribute.
print(harry.language, harry.salary)

# instance attribute takes preference over class attributes .



