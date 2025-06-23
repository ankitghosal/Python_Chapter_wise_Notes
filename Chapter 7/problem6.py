# program to calculate the factorial of a given number using for loop
# 5! = 1 X 2 X 3 X 4 X 5

n = int(input("Enter a number: ")) 
product = 1
for i in range(1, n+1):
    product = product * i

print(f"The factorial of {n} is {product}")

# using while loop:

n = int(input("Enter a number: ")) 

i = 1
product = 1
while(i<=n):
    product *= i
    i += 1
print(f"The factorial of {n} is {product}")






