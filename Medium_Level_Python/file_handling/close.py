# Closing Files Automatically Using with Statement in Python

# The with statement provides a way for ensuring that a resource is properly released after its use
with open('../file_handling/example', 'r') as file:
    content = file.read()
    print(content)

# No need to explicitly call file.close(), it's automatically done by the with statement

# This script demonstrates the recommended way of handling file opening and closing in Python using the with statement.
