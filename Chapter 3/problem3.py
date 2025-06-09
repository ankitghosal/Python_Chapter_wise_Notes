# detect duoble space in a string

a = "Harry is a good  boy  and "

print(a.find("  "))   # after 15 step on  16 step is the first double space.
print(a.find("goo"))

# replace double space with single space.

print(a.replace("  ", " "))
