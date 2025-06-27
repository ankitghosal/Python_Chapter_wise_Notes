#program to filter a list of numbers which are divisible by 5

def divisible(n):
    if(n%5 == 0):
        return True
    return False

a = [1, 2, 3455566, 6556, 676, 70, 89]

f = list(filter(divisible, a))
print(f)


