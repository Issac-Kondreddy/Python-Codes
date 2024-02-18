# Opening Files in Python

# To open a file, use the open() function. It requires at least one argument: the file path.
# The mode argument is optional and specifies the mode in which the file is opened.

# Opening a file for reading ('r' mode is default)
file = open('../file_handling/example', 'r')
print("File opened in read mode.")

# Opening a file for writing ('w' mode). This will create the file if it does not exist.
file = open('../file_handling/example', 'w')
print("File opened in write mode.")

# Always make sure to close your files to free up system resources.
file.close()

# This script demonstrates how to open files in different modes with Python's open() function.
