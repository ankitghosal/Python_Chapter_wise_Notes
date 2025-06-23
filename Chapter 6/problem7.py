# write a program to find out whether a given post is talking about "Harry" or not.



text = input("Enter your texts here: ")

if("Harry".lower() in text.lower()):     # allows any spellingof harry( Harry/ haRry/ harrY) anything
    print("The text is talking about Harry.")

else:
    print("The text is not talking about Harry.")
