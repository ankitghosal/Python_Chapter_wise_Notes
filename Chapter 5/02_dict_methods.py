marks = {                                     
    "Harry": 100,                           
    "Subham": 56,                         
    "Rohan": 34,
    0: "Harry"                          
} 

# print(marks.items()) - prints as individual tuples
# print(marks.keys())  #- prints only keys
# print(marks.values()) - prints only values
# marks.update({"Harry": 99, "Renuka": 100})  - updates the dictionary
print(marks)

'''print(marks.get("Harry2"))  #even though seems same but Prints None
print(marks["Harry2"])   # returns an error'''

for key, values in marks.items():
    print(key, values, sep =" - ")
