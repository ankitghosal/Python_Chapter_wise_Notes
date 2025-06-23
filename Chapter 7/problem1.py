# program to print multiplication table of a number using loop.

n = input("Enter a number: ")

for i in range(1, 11):
    print(f"{n} X {i} = {n * i} ")

# because you didn't mention input as int
''' Correct table: '''
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{n} X {i} = {n * i} ")
