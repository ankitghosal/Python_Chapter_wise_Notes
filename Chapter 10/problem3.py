# Create a class with a class attribute a; create an object from it and set 'a' directly using object.a=0.
# Does this change the class attribute ?

class Demo:
    a = 4

o = Demo()
print(o.a) # prints Class attribute bcz Instance attribute is not present.

o.a = 0 # Instane attribute is set.
print(o.a) # prints Instance attribute bcz Instance attribute is present.

''' But this doesn't change class attribute. bcz when we change object and put demo
it again returns value.
thus, Value of a didn't change.'''

print(Demo.a)


  