class Employee:
    language = "Py" # this is a class attribute.
    salary = 120000

# These are the two employees who fall in this class
harry = Employee()
harry.name = "Harry" # this is a instance attribute.
print(harry.name, harry.language, harry.salary)

rohan = Employee()
rohan.name = "Rohan Roro Robinson"
print(rohan.name, rohan.salary, rohan.language)


# Here name is instance attribute and salary and language are class attributes 
# as they directly belong to class 




