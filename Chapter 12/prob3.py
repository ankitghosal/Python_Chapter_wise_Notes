# a List comprehensin to print a list which contains the multiplicatin table of a user entered number.

n = int(input("Enter a number: "))

table = [n * i for i in range(1, 11)]
print(table)


