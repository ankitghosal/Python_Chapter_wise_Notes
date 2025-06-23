# rename a file to "renamed_by_python.txt"

with open("old.txt") as f:
    content = f.read()

with open("renamed_by_python.txt", "w") as f:
    f.write(content)

# this just renames the old file. But the old file remains. 
# Old file can be deleted by OS module. not used here this time.
