#print 3rd, 5th & 7th element from a list using enumerate function.

l = [1, 2, 3, 4, 5, 6, 7, 8]

for i, item in enumerate(l):
    if i == 2 or i == 4 or i == 6:  # 2, 4, 6 are the index value( staring from 0)
            print(item)

            