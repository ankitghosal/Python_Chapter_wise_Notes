try:
    a = int(input("Hhey, Enter a number: "))

except ValueError as v:
    print("Heyyy")
    print(v)

except Exception as e:
    print(e)

print("Thank You")

