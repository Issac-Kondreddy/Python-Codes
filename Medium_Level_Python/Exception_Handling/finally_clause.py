# Finally Clause in Python

# The finally block lets you execute code, regardless of the result of the try- and except blocks.

try:
    file = open('../file_handling/example', 'r')
    # Attempt to read the file
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found.")
finally:
    # This block will run whether or not the try block raises an error
    print("Cleaning up resources...")
    file.close()

# The finally clause is useful for resource management tasks such as closing files or releasing external resources.

