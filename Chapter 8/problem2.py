# using ffunction convert Celcius to Fahrenheit

# c/5 = (f-32)/9

f = int(input("Enter temperature in F: "))
c = 5*(f-32)/9

print(c)

""" Now to do it with function"""

def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter temperature in F: "))
c= f_to_c(f) # for easy readibility
print(f"{round(c, 2)}°C")

