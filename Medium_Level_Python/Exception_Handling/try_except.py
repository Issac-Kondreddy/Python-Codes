# Try and Except in Python

# The try block lets you test a block of code for errors.
# The except block lets you handle the error.

try:
    # Try to open a non-existent file
    file = open('nonexistent_file.txt', 'r')
except FileNotFoundError:
    # This block runs if the FileNotFoundError is raised
    print("File not found error caught!")

# You can handle multiple exceptions by specifying them in a tuple
try:
    # Division by zero error
    division = 10 / 0
except (FileNotFoundError, ZeroDivisionError):
    print("Caught an error!")

# This script demonstrates using try and except blocks to catch and handle exceptions in Python.
