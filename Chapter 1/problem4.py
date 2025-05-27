# Write a python program to print the contents of a directory using OS module.
# Search online for the functiuon which does that.
# We'll use chatgtp for this



import os

def print_directory_contents(directory):
    try:
        # List all the files and directories in the given directory
        contents = os.listdir(directory)
        
        # Print the contents
        for item in contents:
            print(item)
    
    except FileNotFoundError:
        print(f"The directory {directory} does not exist.")
    except PermissionError:
        print(f"Permission denied to access the directory {directory}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the directory you want to print the contents of
directory_path = '/'

# Call the function
print_directory_contents(directory_path)


