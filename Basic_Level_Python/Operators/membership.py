# Membership Operators in Python

# Membership operators are used to test if a sequence is presented in an object:
# in, not in

# Example list and string
my_list = [1, 2, 3, 4, 5]
my_string = "Hello, world!"

# Using 'in' operator
# Checks if a value is present in the list or string
print(f'3 in my_list: {3 in my_list}')  # Outputs: True
print(f'"Hello" in my_string: {"Hello" in my_string}')  # Outputs: True

# Using 'not in' operator
# Checks if a value is not present in the list or string
print(f'6 not in my_list: {6 not in my_list}')  # Outputs: True
print(f'"Python" not in my_string: {"Python" not in my_string}')  # Outputs: True

# These operators are useful for conditional statements to check for presence or absence of a value in data structures like lists, tuples, strings, and dictionaries.
