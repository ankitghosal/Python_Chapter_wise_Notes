a = input("Please Enter a Name: ")
b = input("please Enter a Date: ")

letter = '''Dear <|name|>,
You are selected!
<|date|>'''

print(letter.replace("<|name|>", a).replace("<|date|>", b))



      