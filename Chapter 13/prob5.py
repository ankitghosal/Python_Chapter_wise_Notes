# find the max of numbers ina list using the reduce function

from functools import reduce
a = [1, 2, 65, 1111, 3455566, 6556, 676, 70, 89]

def greater(a, b):
    if (a>b):
        return a
    return b

print(reduce(greater, a))


