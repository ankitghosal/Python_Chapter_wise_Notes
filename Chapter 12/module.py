def myFunc():
    print("Hello World")


if __name__ == "__main__":
    # if this code is directly executed by running the file it's present in
    print("We are directly running this code.")

myFunc()
print(__name__) # if it is run from here returns -> main
                # if run from imported file(main.py), returns -> module



                