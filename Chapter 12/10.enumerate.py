l = [3, 523, 53, 535]

# index = 0
# for item in l:
#     print(f"The item number at index {index} is {item}")
#     index += 1

''' Can be simplified with enumerate func'''

for index, item in enumerate(l):
    print(f"The item number at index {index} is {item}")

