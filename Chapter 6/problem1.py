# a program to find the greatest of four numbers entered by the user.

a1 = int(input("Enter Number 1: "))
a2 = int(input("Enter Number 2: "))
a3 = int(input("Enter Number 3: "))
a4 = int(input("Enter Number 4: "))

if(a1>a2 and a1>a3 and a1>a4):
    print("Greatest number is a1:", a1)

if(a2>a1 and a2>a3 and a2>a4):
    print("Greatest number is a1:", a2)

if(a3>a2 and a3>a1 and a3>a4):
    print("Greatest number is a1:", a3)

if(a4>a2 and a4>a3 and a4>a1):
    print("Greatest number is a1:", a4)
