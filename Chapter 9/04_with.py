f = open("myyfile.txt")
print(f.read())
f.close()

# The same can be written using with statement like this:
with open("file.txt") as f:
    print(f.read())

# you don't have to explicitly close the file






