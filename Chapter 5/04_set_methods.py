s = {1, 5, 32, 54, 5, 5, 5, "Harry"} # no repititiion allowed
print(s, type(s))  # no way to change items in set

s.add(566)
print(s, type(s))
s.remove(5)
print(s, type(s))