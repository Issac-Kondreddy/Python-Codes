# Reading Files in Python

# Opening a file in read mode and reading its contents
file = open('../file_handling/example', 'r')

# Reading the entire file content
content = file.read()
print("File content:")
print(content)

# It's good practice to close the file when you're done with it
file.close()

# Reading lines from a file
file = open('../file_handling/example', 'r')
for line in file:
    print(line, end='')  # end='' prevents adding an extra newline as print adds one by default

file.close()

# This script demonstrates reading the entire content of a file and reading it line by line.
