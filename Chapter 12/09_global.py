a = 89 # global variable

def fun():
    global a # changing the previous global a
    a = 3 # local variable for this function
    print(a)


fun()
print(a)

