# Identity Operators in Python

# Identity operators compare the memory locations of two objects:
# is, is not

# Example variables
a = [1, 2, 3]  # List a
b = a           # b is the same list
c = [1, 2, 3]  # List c, same values as a but a different object

# Using 'is' operator
# Checks if both variables point to the same object
print(f'a is b: {a is b}')  # Outputs: True because b is the same object as a
print(f'a is c: {a is c}')  # Outputs: False because c is an identical list, but a separate object in memory

# Using 'is not' operator
# Checks if both variables do not point to the same object
print(f'a is not c: {a is not c}')  # Outputs: True

# The identity operators are particularly useful for checking if variables refer to the same object in memory, not merely if they are equal.
# This can be important for performance considerations and when you're working with mutable objects.
