# program to print multiple table of n using for loop in reverse order.

'''
1 10
2 9
3 8
4 7
5 6
6 5
7 4
8 3
9 2
10 1            so range (1, 11),  n X (11 - i)
'''

n = int(input("Enter row number: ")) 

for i in range(1, 11):
    print(f"{n} X {11 - i} = {n*(11-i)}")

# using while loop:

n = int(input("Enter row number: ")) 

i = 1

while(i<11):
    print(f"{n} X {11-i} = {n*(11-i)}")
    i += 1
    

