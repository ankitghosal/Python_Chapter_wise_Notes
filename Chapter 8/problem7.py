# a function to remove a given word from a list and strip it at the same time.

def rem(l, word):
    for item in l:
        l.remove(word)
        return l

l = ["Harry", "Rohan", "Shubham", "an"]

print(rem(l, "an"))

# Now to remove "an" even from names - 

def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n

l = {"Harry", "Rohan", "Shubham", "an"}

print(rem(l, "an"))



