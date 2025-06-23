# Read the text from a given file 'poem.txt' and find out whether it contains the word 'twinkle'.

f = open("poem.txt")
content = f.read()
if("twinkle" in content):
    print("The word Twinkle is present in the content.")
else:
    print("The word Twinkle is NOT present in the content.")

f.close()



