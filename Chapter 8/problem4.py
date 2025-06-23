# Write a recursive function to calculate the sum of first n natural numbers.

'''
sum(n) = 1 + 2 + 3 + 4 + .... + n
sum(n) = sum(n-1) + n
'''

def sum(n):
    if (n==1):
        return 1

    else:   
        return sum(n-1) + n

print(sum(5))
