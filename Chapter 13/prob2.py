# input name, marks & phone number of a student nd format itusing format function like below:
# " The name of the Student is Harry, his marks are 72 and phone number is 9999988876" 

name = input("Enter name: ")
marks = int(input("Enter Marks: "))
phone_number = int(input("Enter phone number: "))

s = "The name of the Student is {}, his marks are {} and phone number is {}".format(name, marks, phone_number)

print(s)
