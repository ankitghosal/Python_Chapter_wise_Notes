friends = ["Apple", "Orange", 5, 345.06, False, "Akash", "Rohan"]
print(friends)

friends.append("Harry")   # append - adds a string at end of a list - more methods in note
print(friends)


l1 = [1, 34, 62, 2, 6, 11]
# l1.sort() - arranges the  list
# l1.reverse() - reverses the list. it doesn't arrange just reverses the arangement.
l1.insert(4, 33333) # insert 3333 such that its index in the list is 3
print(l1.pop(3)) # will print at index 3 and will return value.
print(l1.remove(62)) # removes 62 from the list
print(l1)
