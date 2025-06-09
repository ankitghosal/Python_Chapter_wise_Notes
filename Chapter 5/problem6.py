# allow 4 friends to enter their favourite language as values and keys as their names.
d = {}

name = input("Enter first friend's name: ")
lang = input("enter Language name: ")
d.update({name: lang})

name = input("Enter Second friend's name: ")
lang = input("enter Language name: ")
d.update({name: lang})

name = input("Enter Third friend's name: ")
lang = input("enter Language name: ")
d.update({name: lang})

name = input("Enter Fourth friend's name: ")
lang = input("enter Language name: ")
d.update({name: lang})                  # if names are same then the next name and lang will be updated
                                            #it'll only give the second updated result

print(d)
                        # if languages are same but names are different - nothing will happen. 
                        # values are same