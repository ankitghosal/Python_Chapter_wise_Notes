'''Print first n lines of following pattern - 
***
**      n = 3
*
'''

def pattern(n):
    if (n==0):
        return
    print("*"*n)
    pattern(n-1)

pattern(5)


