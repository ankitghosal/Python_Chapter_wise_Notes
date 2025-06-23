# repeat prob 4 for a list of such words to be censored.


words = ["Donkey", "bad", "ganda"]

with open("file2.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))   # changed contentNew to Content - to directly change the main content.

with open("file2.txt", "w") as f:
    f.write(content)

