# a program to find whether a given number is prime or not.

n = int(input("Enter a number: "))   #[ Prime numbers - divisible with 1 ot that number only]

for i in range(2, n):
    if(n%i) == 0:
        print("Number is not Prime")
        break

else:
    print("Number is prime")





